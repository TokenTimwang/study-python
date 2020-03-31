#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: jenkins-core.py
# @Time    : 2020/3/31 21:51
"""

"""
Installing:
    pip install python-jenkins
    

url: https://python-jenkins.readthedocs.io/en/latest/api.html

Import:

    import jenkins
"""
import jenkins


class JzPythonJenkins(object):

    def __init__(self):
        username = 'xxxxx'
        password = 'xxxxx'
        url = 'http://localhost:8080/jenkins/'
        timeout = 1
        self.server = self.Connect(url, username, password, timeout)

    def used(self):
        self.get_version()

    def connect(self, url, username, password, timeout):
        """Create handle to Jenkins instance"""
        self.server = jenkins.Jenkins(url, username, password, timeout)
        return self.server

    def get_whoami(self):
        self.server.get_whoami()

    def get_version(self):
        """get jenkins version"""
        version = self.server.get_version()
        print(version)

    def job(self):
        # 创建Project,内容为空
        self.server.create_job('test', jenkins.EMPTY_CONFIG_XML)

        # job构建empty
        self.server.build_job('empty')

        # 获取job配置 prints XML configuration
        my_job = self.server.get_job_config('empty')
        print(my_job)

        # 禁用Project
        self.server.disable_job('empty')

        # 拷贝Project
        self.server.copy_job('empty', 'empty_copy')

        # 启用已配置好Project
        self.server.enable_job('empty')

        # 删除Project
        self.server.delete_job('empty')

    def view(self):
        # 创建空视图
        self.server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)

        # 获取视图的配置xml信息
        view_config = self.server.get_view_config('EMPTY')

        # 获取视图信息
        views = self.server.get_views()
        print(views)

        # 删除视图
        self.server.delete_view('EMPTY')

    def plugins(self):
        # 获取插件信息
        plugins = self.server.get_plugins_info()
        print(plugins)

    def node(self):
        # 创建node节点
        self.server.create_node('slave123456')

        ## create node with parameters
        params = {
            'port': '22',
            'username': 'juser',
            'credentialsId': '10f3a3c8-be35-327e-b60b-a3e5edb0e45f',
            'host': 'my.jenkins.slave11'
        }
        ## 名称,描述,远程工作目录,标签,用法，启动方法(连接方式),参数(如host)
        self.server.create_node(
            'slave11',
            nodeDescription='my test slave',
            remoteFS='/home/juser',
            labels='precise',
            exclusive=True,
            launcher=jenkins.LAUNCHER_SSH,
            launcher_params=params)

        # 获取node信息
        nodes = self.server.get_nodes()
        print(nodes)

        # 获取node配置信息
        node_config = self.server.get_node_info('slave123456')
        print(node_config)

        # 连接或中断node
        self.server.disable_node('slave11')
        self.server.enable_node('slave11')

    def queue(self):
        # 获取信息
        queue_info = self.server.get_queue_info()
        print(queue_info)


if __name__ == "__main__":
    JzPythonJenkins = JzPythonJenkins()
    # JzPythonJenkins.get_whoami()
    # JzPythonJenkins.Used()
    JzPythonJenkins.node()
