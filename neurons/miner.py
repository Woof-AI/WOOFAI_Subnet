# MIT License
# Copyright © 2023 Yuma Rao
import os
import time
import typing
import bittensor as bt
import requests
import base64

# Bittensor Miner Template
import template
from template.base.miner import BaseMinerNeuron

class Miner(BaseMinerNeuron):
    def __init__(self, config=None):
        super(Miner, self).__init__(config=config)
        
        
        self.api_url = os.getenv('AI_API_URL', 'https://localhost:8000') + "/predict"

    async def forward(
        self, synapse: template.protocol.DogSoundProtocol
    ) -> template.protocol.DogSoundProtocol:

        try:
            # 记录开始时间
            start_time = time.time()
            
            # 将Base64音频数据转换为二进制
            audio_binary = base64.b64decode(synapse.audio_data)
            
            # 准备文件数据
            files = {
                'file': ('recording.wav', audio_binary, 'audio/wav')
            }
            
            # 调用AI服务
            response = requests.post(self.api_url, files=files)
            response_json = response.json()
            
            # 计算响应时间
            response_time = time.time() - start_time
            
            # 解析结果
            synapse.is_dog_sound = response_json['result'] == "狗叫"
            synapse.probability = response_json['probability']
            synapse.response_time = response_time
            
            bt.logging.debug(f"识别结果: {response_json['result']}, 概率: {response_json['probability']}")
            
        except Exception as e:
            bt.logging.error(f"处理请求时发生错误: {str(e)}")
            # 发生错误时设置默认值
            synapse.is_dog_sound = False
            synapse.probability = 0.0
            synapse.response_time = 0.0
            
        return synapse

    async def blacklist(
        self, synapse: template.protocol.DogSoundProtocol
    ) -> typing.Tuple[bool, str]:

        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            return True, "Missing dendrite or hotkey"

        uid = self.metagraph.hotkeys.index(synapse.dendrite.hotkey)
        
        # 检查是否是注册的热键
        if (
            not self.config.blacklist.allow_non_registered
            and synapse.dendrite.hotkey not in self.metagraph.hotkeys
        ):
            return True, "Unregistered hotkeys"

        # 检查是否强制要求验证者许可
        if self.config.blacklist.force_validator_permit:
            if not self.metagraph.validator_permit[uid]:
                return True, "Non-validator hotkeys"

        return False, "Certified Hotkeys"

    async def priority(self, synapse: template.protocol.DogSoundProtocol) -> float:
        if synapse.dendrite is None or synapse.dendrite.hotkey is None:
            return 0.0

        caller_uid = self.metagraph.hotkeys.index(synapse.dendrite.hotkey)
        priority = float(self.metagraph.S[caller_uid])
        
        bt.logging.trace(f"Request Priority {synapse.dendrite.hotkey}: {priority}")
        return priority

# 主函数
if __name__ == "__main__":
    with Miner() as miner:
        while True:
            bt.logging.info(f"Miner running... {time.time()}")
            time.sleep(5)
