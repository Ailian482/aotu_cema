"""
1. TestLog：日志记录和管理功能，z针对不同情况，设置不同的日志级别，方便定位问题
2. Report：测试报告生成和管理以及及时通知，测试结果快速响应
3. Config：配置文件、静态资源的管理，遵循高内聚低耦合的原则
4. Public：公共函数、方法以及通用操作的管理，遵循高内聚低耦合的原则
5. case：测试用例管理功能，一个功能点对应一条或者多条case，尽可能的提高覆盖率
6. PageElements：测试数据管理功能，数据与脚本分离，降低维护成本，提高可移植性
7. TestSuite：测试组件管理功能，针对不同场景不同需求，组装构建不同的测试框架，遵循测试框架的灵活性和可扩展性
8. TestStatistics：测试结果统计管理功能，每次执行测试的结果统计、分析、对比以及反馈，数据驱动，为软件优化和流程改进提供参考
9. TestRunner.py：持续集成环境，即CI环境，包括测试文件提交、扫描编译、执行测试、生成报告及时通知等功能，持续集成是自动化测试框架的核心
"""
