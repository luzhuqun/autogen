import autogen

config_list = [ { 'model': 'gpt-4-1106-preview', 'api_key': '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' } ]

llm_config={
    "seed": 42,  #为缓存做的配置
    "config_list": config_list
}
# 用户代理agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy", # agent的标识符
    system_message="A human admin.",  # 系统消息是用户给代理的角色
    code_execution_config={"last_n_messages":2, "work_dir":"groupchat"}, # 工作目录设置为groupchat
    human_input_mode="NEVER"
)
# 助理agent
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in product ideas.",
    llm_config=llm_config,
)

# GroupChatManager
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[],max_round=12) # 群聊 最大的chat轮次12次
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)  #管理员，可以与之交互

user_proxy.initiate_chat(manager,
message="Query finance news on https://www.baidu.com/?tn=news, random pick one, scrap the article content, and form a post for writing a blog")
