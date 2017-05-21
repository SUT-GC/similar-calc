# 基于字符串匹配的新店铺判重算法研究与实现

## 摘要

每个外卖平台都存在自己的“商户字典系统”，该系统是现有外卖平台的所有商户数据的集合。其真正存在的意义就在于：一条商户数据便代表现实世界中一家支持外卖的实体商户。这些数据的存在对一家外卖平台来说有着极其重要的商业价值，既然商户字典是世界中所有商户的集合，那么合作店（已经在该平台开店）和商机（还未在该平台开店）一目了然，外卖平台可以有针对性的对这些商机进行拜访，使其成为外卖平台的使用者，提高该平台的市场占用率。

“商户字典系统”既然是所有商户数据的集合，他的数据必然不是一个平台所能提供的，商户字典系统是拿到所有外卖平台的数据进行整合所得到的数据系统。而既然其意义是：一条商户数据代表现实世界中一家支持外卖的实体商户，这么多平台数据必然存在交集（比如A店铺在饿了么上已经开店，在美团外卖上也已经开店，当拿到饿了么的所有店铺数据和美团外卖的所有店铺数据时，A店铺就是交集数据），处理交集数据是“商户字典系统”开发者所要面临的巨大难题之一。

本课题便是要多所有外卖平台的店铺数据特性进行分析，研究出一套基于“字符串匹配算法”的新店铺判重算法。使用该算法可以精准的将上文所述的“交集数据”进行合理的计算，将多份重复店铺数据进行判重，根据优先级选出一条最需要的数据进行保留，使“商户字典系统”数据更加准确。

对“新店铺判重算法”的研究和实现采用的是Python程序设计语言进行数据的分析研究，字符串匹配算法的挑选，分析图的绘制。并且利用PostgreSql数据库的地理特性对数据进行快速准确的索引。最终利用Java程序设计语言和Python程序设计语言将整套门店判重算法进行打包，最终实现一套完整的新店铺判重算法。在数据分析和程序设计期间，还会用到很多算法包：比如JaroWinkler算法包，Levenshtein算法包，LongestCommonSubsequence算法包； 很多工具包：maplotlib绘图包，numpy数据分析包：sqlalchemy ORM框架包；

## Abstract

> 摘要最终整理好之后，再对摘要进行英文翻译

## 目录

## 第1章 绪论

### 1.1 课题研究的目的及意义

#### 1.1.1 研究的目的

“饿了么商户数据字典” (Eleme Dictionary of Merchant，以下简称DOM)模块，是饿了么公司
的“商户数据字典”，存储了现有所有外卖平台(包括饿了么，百度外卖，美团外卖，点评外卖等)的商户基本信息数据，其真正存在的意义便是DOM中的每一条数据记录，都代表着现实世界中一家支持外卖的实体商户。因此，DOM对于“饿了么”有很高的战略意义。DOM中的数据主要分两种，一种是已合作店铺（该店铺在饿了么平台上已经开了虚拟店），一种是潜在商机（该店铺还没有在饿了么平台上开设虚拟店）。DOM中数据的准确性对于“饿了么”外卖平台来说也是至关重要的，特别是潜在商机的准确性与覆盖率。高准确性和高覆盖率可以让“饿了么”市场BD人员准确的开拓市场，高效率的占有市场份额。

因为DOM的数据是集所有外卖平台店铺数据于一体，也因此会出现“商户数据字典”系统该面对数据交集问题，即一家实体店铺在不止一个外卖平台上都有开店，导致同一家实体店的数据会因为开店平台不同，落入多份数据到DOM库中，这与DOM存在的意义(现实世界中一家实体店仅仅对应DOM中一条数据记录)相违背，由此使用“店铺判重算法”来无效掉重复的门店信息将成为解决上一问题的唯一途径。DOM中现在使用的“店铺判重算法”准确率极低(≤ 50%)，导致DOM库中的数据不能与本身存在的意义相匹配。而也因为这些脏数据的问题给下游数据消费者带来极大的不便，在公司战略上造成了一定的影响。所以，研发一套新的“店铺判重算法”对 DOM 来说至关重要。

#### 1.1.2 研究的意义

本课题研究的意义就在于为“饿了么”DOM系统提供一套新的“店铺判重算法”，提高判重的准确率，确保店铺数据在DOM中的唯一性，由此来为下游消费者提供更好，更准的数据支持，为公司在开店战略上提供数据保证。DOM中的数据干净，将为市场人员节省大量工作时间，将会帮助公司更好的抢占市场份额，为“饿了么”成为真正的外卖平台强者出一份力，也更快的让“饿了么”愿景：美好生活，触手可得，早日实现。

### 1.2 课题研究的主要任务和预期目标

#### 1.2.1 主要任务

在互联网行业飞速发展的今天，各种信息资源，知识内容通过互联网已经充分且迅速的到达充满整个世界，我们主要任务是充分利用互联网资源和自身掌握的计算机程序知识来重新设计一套“店铺判重算法”。为此，公司将会提供各种技术及数据上的支持，比如：10万数量级的店铺基本信息，包括美团外卖平台上、点评外卖平台上、百度外卖平台上、饿了么平台上店铺基本信息。我们要分析其数据特性，配合上现在现有的技术和算法，包括字符串匹配算法，研发出准确率高，可靠性强的“新店铺判重算法”。

#### 1.2.2 预期目标

要求研发出来的“新店铺判重算法”将会判断任意两家虚拟店铺信息在现实世界中是否是同一家实体店铺，而准确率要高于80%，即有100对正常虚拟店铺，能准确判断出80对以上是否重复(一对中的两家店是否是同一家实体店)

## 第2章 关键技术介绍

### 2.1 Python 语言介绍

#### 2.1.1 Python 语言简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

* Python 是一种解释型语言： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
* Python 是交互式语言： 这意味着，您可以在一个Python提示符，直接互动执行写你的程序。
* Python 是面向对象语言: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
* Python 是初学者的语言：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

#### 2.1.2 Python 发展历史

Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。

Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。

像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。

现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。

#### 2.1.3 Python 语言的特点

* 易于学习：Python有相对较少的关键字，结构简单，和一个明确定义的语法，学习起来更加简单。
* 易于阅读：Python代码定义的更清晰。
* 易于维护：Python的成功在于它的源代码是相当容易维护的。
* 一个广泛的标准库：Python的最大的优势之一是丰富的库，跨平台的，在UNIX，Windows和Macintosh兼容很好。
* 互动模式：互动模式的支持，您可以从终端输入执行代码并获得结果的语言，互动的测试和调试代码片断。
* 可移植：基于其开放源代码的特性，Python已经被移植（也就是使其工作）到许多平台。
* 可扩展：如果你需要一段运行很快的关键代码，或者是想要编写一些不愿开放的算法，你可以使用C或C++完成那部分程序，然后从你的Python程序中调用。
* 数据库：Python提供所有主要的商业数据库的接口。
* GUI编程：Python支持GUI可以创建和移植到许多系统调用。
* 可嵌入: 你可以将Python嵌入到C/C++程序，让你的程序的用户获得"脚本化"的能力。

### 2.2 Sqlalchemy 框架介绍

#### 2.2.1 Sqlalchemy 简介

SQLAlchemy是Python编程语言下的一款开源软件。提供了SQL工具包及对象关系映射（ORM）工具，使用MIT许可证发行。

SQLAlchemy“采用简单的Python语言，为高效和高性能的数据库访问设计，实现了完整的企业级持久模型”。SQLAlchemy的理念是，SQL数据库的量级和性能重要于对象集合；而对象集合的抽象又重要于表和行。因此，SQLAlchmey采用了类似于Java里Hibernate的数据映射模型，而不是其他ORM框架采用的Active Record模型。不过，Elixir和declarative等可选插件可以让用户使用声明语法。

SQLAlchemy首次发行于2006年2月，并迅速地在Python社区中最广泛使用的ORM工具之一，不亚于Django的ORM框架。

#### 2.2.2 Sqlalchemy 架构

SQLAlchemy 很有特色的一点就是它刻意被分为另种用法，就是 CORE 和 ORM，这是由它的架构决定的。

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/sqlalchemy_core.jpg)

这样的架构的好处是带来了 Core 与 ORM 的解耦和，当我们需要高性能的 SQL 执行但又不想抛弃 SQLAlchemy 带来的session管理、连接池管理、数据库“中立”的语句编写等这些好处时我们可以直接用 CORE。直接用 CORE 是什么意思呢？我们看到架构里只有Rational Mapper在 CORE 之上，实际也确实如此，因为Schema、SQL Expression Language还在 CORE 内，所以使用 CORE 可以直接写纯 SQL 语句，我们称之为Raw SQL的写法，也可以用SQL Expression，后者因为是相当于写 Python 代码，所以可以带来更好地阅读性和可维护性，不过Raw SQL更灵活，所以在很复杂的语句面前Raw SQL就更占优势了。

再往下看这个图，我们可以看到 DBAPI 是由Third party libraries实现的，也就是说 SQLAlchemy 并没有提供直接连接数据库的功能，而是通过第三方实现。

![图片来源网络](http://oppz2fvil.bkt.clouddn.com/sqlalmchey_connect.jpg)

SQLalchemy 对dialect支持很全，就以常见的 MySQL 为例，可以支持：MySQL-Python、OurSQL、PyMySQL、MySQL Connector/Python、CyMySQL、Google Cloud SQL、PyODBC、zxjdbc for Jython，具体可以在 SQAlchemy 的dialects页面里查到。

这样有什么坏处呢，最明显的就是低效。因为传统 Python 解释器 CPython 的实现原因（主要是 C 的问题）长的函数调用栈会带来显着地性能问题。 由于路径过长，不可避免地导致运行时的缓慢。SQLAlchemy 花了很旧去缩短调用路径和通过 C 代码处理性能瓶颈，效果还不错，不过最好还是希望 PyPy 能够广泛流行起来，通过JIT缓解这个问题。

![图片来源网络](http://oppz2fvil.bkt.clouddn.com/sqlalchemy_engine.jpg)

上面的图还是一张抽象程度比较高的，下面我细节点的介绍下 SQLAlchemy 的Engine。

![图片来源网络](http://oppz2fvil.bkt.clouddn.com/sqlalchemy_schema.jpg)

对于使用者来说，Engine是核心，因为Connection、 ResultProxy这些都是在Engine之后生成的，建立Engine则有两个重点，就是Pool和Dialect，前者是做连接池管理，后者则负 责与 DBAPI 的沟通，如同其名字所示，负责“方言”与“普通话”的翻译。上图是以psycopg2为例的，使用 MySQL（PyODBC）也是类似的。

### 2.3 Maplotlib 工具包介绍

Matplotlib 是一个 Python 的 2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形。

通过 Matplotlib，开发者可以仅需要几行代码，便可以生成绘图，直方图，功率谱，条形图，错误图，散点图等。

如下图，都是Maplotlib 做出来的。

![图片来源网络](http://oppz2fvil.bkt.clouddn.com/matplotlib.png)

### 2.4 NumPy 工具包介绍

NumPy系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。据说NumPy将Python相当于变成一种免费的更强大的MatLab系统。

它一个用python实现的科学计算包。包括：1、一个强大的N维数组对象Array；2、比较成熟的（广播）函数库；3、用于整合C/C++和Fortran代码的工具包；4、实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。

NumPy（Numeric Python）提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如：Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。

### 2.5 PostgreSQL 数据库介绍

#### 2.5.1 数据库简介

PostgresQL是以加州大学伯克利分校计算机系开发的 POSTGRES，现在已经更名为PostgreSQL，版本 4.2为基础的对象关系型数据库管理系统（ORDBMS）。PostgreSQL支持大部分 SQL标准并且提供了许多其他现代特性：复杂查询、外键、触发器、视图、事务完整性、MVCC。同样，PostgreSQL 可以用许多方法扩展，比如，通过增加新的数据类型、函数、操作符、聚集函数、索引。免费使用、修改、和分发 PostgreSQL，不管是私用、商用、还是学术研究使用。

#### 2.5.2 主要特点

PostgreSQL 的特性覆盖了 SQL-2/SQL-92 和 SQL-3/SQL-99，首先，它包括了可以说是目前世界上最丰富的数据类型的支持，其中有些数据类型可以说连商业数据库都不具备， 比如 IP类型和几何类型等；其次，PostgreSQL 是全功能的自由软件数据库，很长时间以来，PostgreSQL 是唯一支持事务、子查询、多版本并行控制系统（MVCC）、数据完整性检查等特性的唯一的一种自由软件的数据库管理系统。 Inprise 的 InterBase 以及SAP等厂商将其原先专有软件开放为自由软件之后才打破了这个唯一。最后，PostgreSQL拥有一支非常活跃的开发队伍，而且在许多黑客的努力下，PostgreSQL 的质量日益提高。

从技术角度来讲，PostgreSQL 采用的是比较经典的C/S（client/server）结构，也就是一个客户端对应一个服务器端守护进程的模式，这个守护进程分析客户端来的查询请求，生成规划树，进行数据检索并最终把结果格式化输出后返回给客户端。为了便于客户端的程序的编写，由数据库服务器提供了统一的客户端 C 接口。而不同的客户端接口都是源自这个 C 接口，比如ODBC，JDBC，Python，Perl，Tcl，C/C++，ESQL等， 同时也要指出的是，PostgreSQL对接口的支持也是非常丰富的，几乎支持所有类型的数据库客户端接口。

#### 2.5.3 PostgreSQL 比 Mysql 的优势

PostgreSQL 数据库对于Mysql数据了而言，具有如下几点优势：

* PostgreSQL 的稳定性极强， Innodb 等引擎在崩溃、断电之类的灾难场景下抗打击能力有了长足进步，然而很多 MySQL 用户都遇到过Server级的数据库丢失的场景——mysql系统库是MyISAM的，相比之下，PG数据库这方面要好一些。
* 任何系统都有它的性能极限，在高并发读写，负载逼近极限下，PG的性能指标仍可以维持双曲线甚至对数曲线，到顶峰之后不再下降，而 MySQL 明显出现一个波峰后下滑（5.5版本之后，在企业级版本中有个插件可以改善很多，不过需要付费）。
* PostgreSQL 多年来在GIS领域处于优势地位，因为它有丰富的几何类型，实际上不止几何类型，PostgreSQL 有大量字典，数组，bitmap等数据类型，相比之下mysql就差很多，instagram就是因为PostgreSQL的空间数据库扩展PostGIS远远强于Mysql spatial。
* PG 的“无锁定”特性非常突出，甚至包括 vacuum 这样的整理数据空间的操作，这个和PGSQL的MVCC实现有关系。
* PG 的可以使用函数和条件索引，这使得PG数据库的调优非常灵活，mysql就没有这个功能，条件索引在web应用中很重要。
* PG有极其强悍的 SQL 编程能力（9.x 图灵完备，支持递归！），有非常丰富的统计函数和统计语法支持，比如分析函数（ORACLE的叫法，PG里叫window函数），还可以用多种语言来写存储过程，对于R的支持也很好。这一点上MYSQL就差的很远，很多分析功能都不支持，腾讯内部数据存储主要是MYSQL，但是数据分析主要是HADOOP+PGSQL（听李元佳说过，但是没有验证过）。
* PG 的有多种集群架构可以选择，plproxy 可以支持语句级的镜像或分片，slony 可以进行字段级的同步设置，standby 可以构建WAL文件级或流式的读写分离集群，同步频率和集群策略调整方便，操作非常简单。
* 一般关系型数据库的字符串有限定长度8k左右，无限长 TEXT 类型的功能受限，只能作为外部大数据访问。而 PG 的 TEXT 类型可以直接访问，SQL语法内置正则表达式，可以索引，还可以全文检索，或使用xml xpath。用PG的话，文档数据库都可以省了。
* 对于WEB应用来说，复制的特性很重要，mysql到现在也是异步复制，pgsql可以做到同步，异步，半同步复制。还有mysql的同步是基于binlog复制，类似oracle golden gate,是基于stream的复制，做到同步很困难，这种方式更加适合异地复制，pgsql的复制基于wal，可以做到同步复制。同时，pgsql还提供stream复制。
* pgsql对于numa架构的支持比mysql强一些，比MYSQL对于读的性能更好一些，pgsql提交可以完全异步，而mysql的内存表不够实用（因为表锁的原因）

### 2.6 Cosine Similar 算法介绍

#### 2.6.1 介绍

Cosine Similar 又称为“余弦相似度”，它是通过测量两个向量的夹脚的余弦值来度量他们之间的相似性。0度角的余弦值是1，而其他任何角度的余弦值都不大于1；并且其最小值是-1。从而两个向量之间的角度的余弦值确定两个向量是否大致指向相同的方向。两个向量有相同的指向时，余弦相似度的值为1；两个向量夹角为90°时，余弦相似度的值为0；两个向量指向完全相反的方向时，余弦相似度的值为-1。这结果是与向量的长度无关的，仅仅与向量的指向方向相关。余弦相似度通常用于正空间，因此给出的值为0到1之间。

注意这上下界对任何维度的向量空间中都适用，而且余弦相似性最常用于高维正空间。例如在信息检索中，每个词项被赋予不同的维度，而一个文档由一个向量表示，其各个维度上的值对应于该词项在文档中出现的频率。余弦相似度因此可以给出两篇文档在其主题方面的相似度。另外，它通常用于文本挖掘中的文件比较。此外，在数据挖掘领域中，会用到它来度量集群内部的凝聚力。

#### 2.6.2 定义

两个向量间的余弦值可以通过使用欧几里得点积公式求出：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/cosine-function.png)

给定两个属性向量， A 和B，其余弦相似性θ由点积和向量长度给出，如下所示

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/cosine-all.png)

给出的相似性范围从-1到1：-1意味着两个向量指向的方向正好截然相反，1表示它们的指向是完全相同的，0通常表示它们之间是独立的，而在这之间的值则表示中间的相似性或相异性。

对于文本匹配，属性向量A和B 通常是文档中的词频向量。余弦相似性，可以被看作是在比较过程中把文件长度正规化的方法。

在信息检索的情况下，由于一个词的频率（TF-IDF权）不能为负数，所以这两个文档的余弦相似性范围从0到1。并且，两个词的频率向量之间的角度不能大于90°。

“余弦相似性”一词有时也被用来表示另一个系数，尽管最常见的是像上述定义那样的。透过使用相同计算方式得到的相似性，向量之间的规范化角度可以作为一个范围在[0,1]上的有界相似性函数，从上述定义的相似性计算如下：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/consine-03.png)

这式子适用于向量系数可以为正或负的情况。或者，用以下式子计算

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/consine-04.png)

这式子适用于向量系数总为正的情况。
虽然“余弦相似性”一词有时会用来表示这个角距离，但实际上很少这样说，因为角度的余弦值只是作为一种计算角度的简便方法而被用到，本身并不是意思的一部分。角相似系数的优点是，当作为一个差异系数（从1减去它）时，产生的函数是一个严格距离度量，而对于第一种意义的“余弦相似性”则不然。然而，对于大多数的用途，这不是一个重要的性质。若对于某些情况下，只有一组向量之间的相似性或距离的相对顺序是重要的，那么不管是使用哪个函数，所得出的顺序都是一样的。

> 参考网站: [Wiki](https://zh.wikipedia.org/wiki/%E4%BD%99%E5%BC%A6%E7%9B%B8%E4%BC%BC%E6%80%A7)

#### 2.6.3 应用

使用Cosine Similar算法进行两个字符串相似度判断可以分为如下几步：

1 使用TF-IDF算法，找出两篇文章的关键词

比如存在下面两个句子：

```
A：我喜欢看电视，不喜欢看电影。
B：我不喜欢看电视，也不喜欢看电影。
```

使用TF-IDF算法，对上面两个句子进行分词处理得到结果：

```
A:我/喜欢/看/电视，不/喜欢/看/电影。
B:我/不/喜欢/看/电视，也/不/喜欢/看/电影。
```

2 将所有的分词合并得到词集：

```
我，喜欢，看，电视，电影，不，也
```

3 计算词频

```
A：我 1，喜欢 2，看 2，电视 1，电影 1，不 1，也 0。
B：我 1，喜欢 2，看 2，电视 1，电影 1，不 2，也 1。
```

4 描述词频向量

```
A：[1, 2, 2, 1, 1, 1, 0]
B：[1, 2, 2, 1, 1, 2, 1]
```

假定A和B是两个n维向量，A是 [A1, A2, ..., An] ，B是 [B1, B2, ..., Bn]运用计算两个向量的Cosine值公式，则A与B的夹角θ的余弦等于：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/consin-07.png)

使用这个公式，我们就可以得到，句子A与句子B的夹角的余弦。

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/cosine-08.png)

余弦值越接近1，就表明夹角越接近0度，也就是两个向量越相似，这就叫"余弦相似性"。所以，上面的句子A和句子B是很相似的，事实上它们的夹角大约为20.3度。"余弦相似度"是一种非常有用的算法，只要是计算两个向量的相似程度，都可以采用它。

> 参考[网站](https://blog.sectong.com/blog/cosine_similarity.html)

### 2.7 JaroWinkler Similar 算法介绍

#### 2.7.1 简介

The Jaro–Winkler distance (Winkler, 1990)是计算2个字符串之间相似度的一种算法。它是Jaro distance算法的变种。主要用于record linkage/数据连接（重复记录）方面的领域，Jaro–Winkler distance最后得分越高说明相似度越大。Jaro–Winkler distance 是适合于串比如名字这样较短的字符之间计算相似度。0分表示没有任何相似度，1分则代表完全匹配。

#### 2.7.2 定义

先来介绍Jaro distances算法最后的得分公式：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-01.png)

其中：

* s1, s2 是要比对的两个字符
* dj 是最后的得分
* m 是要匹配的字符数
* t 是换位的数目

接着来介绍Match Window(匹配窗口)计算公式

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-02.png)

* s1、s2 是要比对的两个字符
* MW是匹配窗口值

现在我们来解释上面的两个公式：

* 字符串s1与字符串s2在做匹配计算时，当两个字符的距离不大于公式二的最后结果(匹配窗口)即认为是匹配的。
* 当s1、s2中字符相匹配但是字符位置不一样时发生换位操作、而公式一中换位的数目t为不同顺序的匹配字符的数目的一半。比如:两个字符串CRATE和TRACE做匹配操作，字符串中仅有'R' 'A' 'E'三个字符是匹配的，即m=3。为什么'C', 'T'不算做是匹配的呢。因为虽然'C', 'T'都出现在两个字符串中，但是通过公式二得出匹配窗口值为 (5/2)-1=1.5。而两个字符串中'C', 'T'字符的距离均大于1.5。所以不算做匹配。因此t=0。在另一组字符串DwAyNE 与 DuANE 。匹配的字符D-A-N-E 在两个字符串中有相同的字符顺序，所以不需要进行换位操作，因此t=0,m=4。

而jaro-winkler distance 算法公式如下：

Jaro-Winkler算法给予了起始部分就相同的字符串更高的分数，它定义了一个 前缀范围p，对于要匹配的两个字符串，如果前缀部分有长度为L的部分字符串相同，则Jaro-Winkler Distance为:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-03.png)

其中：

* dj是Jaro distance最后得分
* L是前缀部分匹配的长度
* P是一个范围因子常量，用来调整前缀匹配的权值，但是P的值不能超过0.25，因 为这样最后得分可能超过1分.Winkler的标准默认设置值P=0.1。 

#### 2.7.3 应用

* 例子1

给出两个字符串 s1 MARTHA 和 s2 MARHTA、我们可以得出：

1 m = 6
2 |s1| = 6 
3 |s2| = 6
4 两组字符T/H和H/T要进行换位操作，因此t=2/2=1

我们可以根据公式一得出Jaro得分：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-05.png)

如果使用Jaro–Winkler，并且取范围因子P=0.1,我们会得出: P=0.1 L=3

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-04.png)

2 例子2

在这个例子中，我们利用图形来说明匹配过程，给出两个字符串S1 DIXON, S2 DICKSONX 得出下面图表：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-09.png)

其中：1 代表匹配命中，0代表无匹配，匹配窗口mw=8/2-1=3，紫色块代表匹配范围，即在匹配窗口之内。

根据图表，我们得出：

* m=4
* |S1| = 5
* |S2| = 8
* t = 0

我们可以根据jaro公式得出：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/jaro-winkler-10.png)

使用jaro-winkler,并且取范围因子p=0.1得出：

P=0.1
L=2

dw = 0.767 + 2 * 0.1 * (1-0.767) = 0.813

> 参考[百度文库](https://wenku.baidu.com/view/5f8a4402bed5b9f3f90f1c97.html)

### 2.8 Levenshtein Similar 算法介绍

#### 2.8.1 介绍

编辑距离最早由俄罗斯科学家 Levenshtein 提出，故又称 "Levenshtein 距离"。其定义为: 给定两个字符串 A 和 B，将 A 通过删除、插入、替换操作转换为 B 所需要的最少操作次数。

比如将 "kitten" 转换为 "sitting" 需要进行如下操作:

替换操作: kitten -> sitten (k -> s)
替换操作: sitten -> sittin (e -> i)
插入操作: sittin -> sitting (SPC -> g)
我们就说 "kitten" 相对 "sitting" 的编辑距离是 3。

编辑距离衡量的是两个字符串之间的差异程度，所以差异程度越小，相似程度就越大了。

#### 2.8.2 求解公式

下面是Levenshtein Similar算法的递归公式:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/levenshtein-01.png)

根据数学公式转换成python代码如下：

```python
# coding: utf-8
import numpy as np


def edit_distance(a, b):
    m, n = len(a), len(b)
    dis_matrix = np.zeros((m+1, n+1), dtype=int)

    # 初始化距离矩阵的第 0 行和第 0 列
    dis_matrix[0, :] = np.arange(n+1)
    dis_matrix[:, 0] = np.arange(m+1)

    # 开始计算
    for idx_a, ch_a in enumerate(a, 1):
        for idx_b, ch_b in enumerate(b, 1):
            cur_dis = None

            dis_left = dis_matrix[idx_a, idx_b-1]
            dis_upper = dis_matrix[idx_a-1, idx_b]
            dis_upper_left = dis_matrix[idx_a-1, idx_b-1]
            if ch_a == ch_b:
                cur_dis = min(dis_left+1, dis_upper+1, dis_upper_left)
            else:
                cur_dis = min(dis_left+1, dis_upper+1, dis_upper_left + 1)

            dis_matrix[idx_a, idx_b] = cur_dis

    return dis_matrix[m, n]

```

由编辑距离转换成相似度可以使用如下公式：

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/levenshtein-02.png)

> 参考[博客](http://www.zmonster.me/2016/03/31/text-similarity-character-based-1.html#orgheadline5)

### 2.9 LCS Similar 算法介绍

#### 2.9.1 介绍

LCS(LongestCommonSubsequence/最长公共子序列)算法：一个数列 ，如果分别是两个或多个已知数列的子序列，且是所有符合此条件序列中最长的，则称为已知序列的最长公共子序列。

#### 2.9.2 定义

对给定序列 A 和 B, 满足以下条件的一个序列 C 被称为 A 和 B 的公共子序列:

C 中每一个元素都对应 A 和 B 中一个元素从 C 中挑选两个元素 CiCi 和 CjCj ，其中 ii 和 jj 表示这两个元素在 C 中的序号(从左至右)，假设这两个元素分别对应 AmAm 和 AnAn ，那么有 (j−i)⋅(n−m)>0(j−i)⋅(n−m)>0，在 B中对应的两个元素同理比如说给定A=A="打南边来了个喇嘛，手里提拉着五斤鳎目", B=B= "打北边来了个哑巴，腰里别着个喇叭"，以下都是 A 和 B 的子序列:

"打边"
"打边来了个"
"边个着"

在所有可能的 C 中，长度最大的即所谓 "最长公共子序列"。上述例子中 A 和 B 的最长公共子序列是: "打边来了个，里着"。如下图所示:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-01.png)

直观感受上，我们可以认为，如果 A 和 B 的最长公共子序列越长，A 和 B 就越相似。这也是用最长公共子序列来度量文本相似程度的思想。

#### 2.9.3 求解方法

要求解 LCS，朴素的想法是将 A 的所有子序列都枚举一遍，看是否是 B 的子序列，然后从中挑选出最长的。对给定字符串 A ，假定其长度为 LL，其所有可能的子序列数量为 ∑Li=1(Li)∑i=1L(Li) 也就是 2L−12L−1 ，所以暴力求解方法的复杂度至少是指数级的，这显然是不可取的。

通常我们用动态规划方法来求解 LCS 问题。

不难发现 LCS 的求解可以按照以下方法来得到:

1 对比 A 和 B 的第一个字符，如果相等，则转入步骤 2，否则转入步骤 3
2 将 A 和 B 的第一个字符记录为 LCS 的第一个字符，求 A 和 B 剩下部分的 LCS (转回步骤1，下同)
3 将 A 去掉第一个字符，用剩下的部分和 B 一起计算 LCS，转入步骤 4
4 将 B 去掉第一个字符，用剩下的部分和 A 一起计算 LCS，转入步骤 5
5 比较第 3 步和第 4 步得到的 LCS，其中较长的就是 A 和 B 的 LCS.

上述过程很明显是一个递归过程，所以可以简单地实现出来。

但其实还是有问题的，那就是递归树的存在导致了大量的重复计算、以及可能存在的栈溢出风险。举个栗子，计算 "hello" 和 "hero" 的过程如下图所示:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-02.png)

可以看到 "lcs('lo', 'o')" 被计算了两次。

解决上面提到的问题的方法是将递归方法改为循环方法。用 mm 表示 A 的长度，用 nn 表示 B 的长度，我们可以构建一个 m×nm×n 的矩阵 DD ，用来保存上面递归过程中计算到的 A 和 B 的公共子序列。

具体方法是， Di,jDi,j 表示去除 A 的前 i 个元素后的子串 A′A′ 和 B 去掉前 j 个元素后的子串 B′B′ 的 LCS。这样我们首先计算 Dm,nDm,n ，然后计算 Dm−1,nDm−1,n 和 Dm,n−1Dm,n−1 ，再计算 Dm−1,n−1Dm−1,n−1，依次类推。为什么可以这么做呢？仔细看看之前提到的递归过程中的 2、3、4 步，以及上面那张计算 "hello" 和 "hero" 的 LCS 的递归树图，可以发现计算最后都可以归结为计算 A 和 B 尾部片段的 LCS 。

我们发现上面的形式话表述不太直观，如果能先计算 D0,0D0,0 是不是更好一些呢？是的，只要把之前提到的递归规则中的 "比较 A 和 B 的第一个字符" 改为 "比较 A 和 B 的最后一个字符" 并对步骤 2、3、4 做出相应的改变即可。

当然实际上我们不会去用一个二维数组来保存计算过程中用到的(非最长)公共子序列，这样虽然很直观，但是在内存使用上有点丑陋。标准的做法是只记录这些公共子序列的长度，计算完整个长度矩阵后，再从最后的位置回溯取得 LCS 。

先观察一下计算 "lcs('hello', 'hero')" 时得到的公共子序列矩阵:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-03.png)

矩阵中出现过的公共子序列有: 'h', 'he' 和 'heo'。从中我们 似乎可以发现这么一个规律: 从上往下逐行查看，这三个公共子序列 第一次 出现的时候，恰好就是 'hello' 和 'hero' 中有字符相等的时候，换成记录长度后，也就对应某个特定的长度值第一次出现的时候。

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-04.png)

就这个例子而言，我们 似乎 可以这样来根据长度矩阵得到 LCS (行/列序号从 0 开始，后同):

* 在第 1 行第 1 列找到 1 ，对应的字符是 'h'
* 在第 2 行第 2 列找到 2 ，对应的字符是 'e'
* 在第 5 行第 4 列找到 3 ，对应的字符是 'o'

这种方法 直观上感觉是对的，但实际上是有问题的 ，下面是计算 'GCGGACTG' 和 'GCCCTAGCG' 时得到的长度矩阵。

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-06.png)

如果按照刚才的做法来反推 LCS ，会得到下面的结果:

* 在第 1 行第 1 列找到 1 ，对应的字符是 'G'
* 在第 2 行第 2 列找到 2 ，对应的字符是 'C'
* 在第 3 行第 7 列找到 3 ，对应的字符是 'G'
* 在第 4 行第 9 列找到 4 ，对应的字符是 'G'
* 第 4 步找到的 'G' 是 'GCCCTAGCG' 的最后一个字符(表中最后一列)，因此停止

实际上真正求得的 LCS 长度应该是 5 ，为 'GCGCG'、'GCACG' 或 'GCCTG'，而不是 'GCGG'。问题出在哪呢？ LCS 可以看成是一个最优解，但到达最优解的路径可能有不止一条，而且局部的最优解并不一定是最优解的组成部分，所以前面提到的贪心方法在有些情况下可以得到正确的结果，但有的情况下就会出错。

正确的做法是从长度矩阵右下角，根据长度矩阵的计算规则往前反推，这样就能保证得到的结果是最长的公共子序列。

先把子序列长度矩阵的计算方法实现:

```python
import numpy as np


def lcs_matrix(a, b):
    m, n = len(a), len(b)
    matrix = np.zeros((m+1, n+1), dtype=int)

    for idx_a, ch_a in enumerate(a, 1):
        for idx_b, ch_b in enumerate(b, 1):
            if ch_a == ch_b:
                matrix[idx_a, idx_b] = matrix[idx_a-1, idx_b-1] + 1
            else:
                matrix[idx_a, idx_b] = max(
                    matrix[idx_a, idx_b-1],
                    matrix[idx_a-1, idx_b]
                )

    return matrix
```

```python
[[0 0 0 0 0 0 0 0 0 0]
 [0 1 1 1 1 1 1 1 1 1]
 [0 1 2 2 2 2 2 2 2 2]
 [0 1 2 2 2 2 2 3 3 3]
 [0 1 2 2 2 2 2 3 3 4]
 [0 1 2 2 2 2 3 3 3 4]
 [0 1 2 3 3 3 3 3 4 4]
 [0 1 2 3 3 4 4 4 4 4]
 [0 1 2 3 3 4 4 5 5 5]]
```

根据长度矩阵的计算规则，可以按照以下步骤来反推出 LCS:

1 首先定位到长度矩阵右下角位置
2 如果当前位置的值为 0 ，则停止；否则转到步骤 3
3 如果当前位置对应的 A 和 B 的元素相等，则向当前位置的左上角后退一步(行号和列号各减 1)，并回到步骤 2，否则转到步骤 4
4 检查矩阵当前位置左边的值和上边的值，跳转到其中值更大的那个位置(如果相等，则在往上和往左中选择一个方向)，回到步骤 2

用代码实现出来大概是这样:

```python
import numpy as np


def lcs_backtrace(a, b, matrix):
    idx_a, idx_b = len(a) - 1, len(b) - 1

    lcs_list = []
    while matrix[idx_a+1, idx_b+1] > 0:
        if a[idx_a] == b[idx_b]:
            lcs_list.append(a[idx_a])
            idx_a -= 1
            idx_b -= 1
        else:
            upper_value = matrix[idx_a, idx_b+1]
            left_value = matrix[idx_a+1, idx_b]
            if upper_value > left_value:
                idx_a -= 1
            else:
                idx_b -= 1

    lcs_list.reverse()
    return lcs_list
```

#### 2.9.4 数学表示与相似度量

求解方法可以用数学语言表示如下:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-07.png)

其中 AiAi 表示 A 的前 ii 个字符组成的字符串，BjBj 同理。

直观上，我们可以认为 A 和 B 的 LCS 越长，那么 A 和 B 就越相似。为了使所有用于比较的 (A, B) 对得到的相似度量能进行横向比较，定义 LCS 相似度为:

![图片来自网络](http://oppz2fvil.bkt.clouddn.com/lcs-08.png)

这样得到的相似度的值就被变换到 [0, 1] 区间中了。

## 第3章 算法研究

### 3.1 数据特性分析

#### 3.1.1 安装PostgreSQL数据库

运行`brew install postgresql`安装postgresql数据库

#### 3.1.2 建表

dom_eleme_restaurant表存储着饿了么店铺的基本信息表，表结构如下：

|列名|类型|备注|
|:--|:--|:--|
|id|int8|主键id|
|eleme_id|int8|饿了么店铺id|
|eleme_name|varchar(255)|饿了么店铺名称|
|eleme_branch_name|varchar(255)|饿了么分店名称|
|eleme_address|varchar(255)|饿了么店铺地址|
|eleme_phone|varchar(255)|饿了么店铺电话|
|eleme_latitude|numeric|饿了么店铺纬度|
|eleme_longitude|numeric|饿了么店铺经度|
|eleme_logo_hash|varchar(512)|饿了么店铺url|
|eleme_is_value|int2|饿了么店铺是否有效|
|created_at|timestamp|创建时间|
|updated_at|timestamp|更新时间|

dom_baidu_restaurant表存储着百度外卖店铺的基本信息表，表结构如下：

|列名|类型|备注|
|:--|:--|:--|
|id|int8|主键id|
|baidu_id|int8|百度外卖店铺id|
|baidu_name|varchar(255)|百度外卖店铺名称|
|baidu_branch_name|varchar(255)|百度外卖分店名称|
|baidu_address|varchar(255)|百度外卖店铺地址|
|baidu_phone|varchar(255)|百度外卖店铺电话|
|baidu_latitude|numeric|百度外卖店铺纬度|
|baidu_longitude|numeric|百度外卖店铺经度|
|baidu_logo_hash|varchar(512)|百度外卖店铺url|
|baidu_is_value|int2|百度外卖店铺是否有效|
|created_at|timestamp|创建时间|
|updated_at|timestamp|更新时间|

dom_dianping_restaurant表存储着点评外卖店铺的基本信息表，表结构如下：

|列名|类型|备注|
|:--|:--|:--|
|id|int8|主键id|
|dianping_id|int8|点评外卖店铺id|
|dianping_name|varchar(255)|点评外卖店铺名称|
|dianping_branch_name|varchar(255)|点评外卖分店名称|
|dianping_address|varchar(255)|点评外卖店铺地址|
|dianping_phone|varchar(255)|点评外卖店铺电话|
|dianping_latitude|numeric|点评外卖店铺纬度|
|dianping_longitude|numeric|点评外卖店铺经度|
|dianping_logo_hash|varchar(512)|点评外卖店铺url|
|dianping_is_value|int2|点评外卖店铺是否有效|
|created_at|timestamp|创建时间|
|updated_at|timestamp|更新时间|

dom_meituan_restaurant表存储着美团外卖店铺的基本信息表，表结构如下：

|列名|类型|备注|
|:--|:--|:--|
|id|int8|主键id|
|meituan_id|int8|美团外卖店铺id|
|meituan_name|varchar(255)|美团外卖店铺名称|
|meituan_branch_name|varchar(255)|美团外卖分店名称|
|meituan_address|varchar(255)|美团外卖店铺地址|
|meituan_phone|varchar(255)|美团外卖店铺电话|
|meituan_latitude|numeric|美团外卖店铺纬度|
|meituan_longitude|numeric|美团外卖店铺经度|
|meituan_logo_hash|varchar(512)|美团外卖店铺url|
|meituan_is_value|int2|美团外卖店铺是否有效|
|created_at|timestamp|创建时间|
|updated_at|timestamp|更新时间|

#### 3.1.3 准备数据

公司提供百万数据量进行数据分析，但是考虑到数据量庞大，如果统计这么庞大的数据，时间会比较长，所以我们随机抽取30w的数据作为实验数据（使用唯一id的尾数为2,7,9三个数字作为选数条件)。

公司提供美团外卖，点评外卖，百度外卖，饿了么四个外卖平台上的店铺数据较为全面，我们选择几个店铺的基础信息属性作为实验数据属性，经过考虑，我们选出几个平台的共同属性：店铺名称，店铺分店名称，店铺地址，店铺电话，店铺经度，店铺纬度，店铺logo的url。通过python脚本将数据从公司数据库中同步到本地数据库中。

同时，公司提供了经过人工审核而确认下来相似店铺的数据xxx条，我们定此关系为关联，即：如果饿了么A店铺和美团B店铺相似，则定义为A与B相关联。经过随机筛选，我们分别抽出美团76000条关联记录（即有7600家饿了么店和美团店铺相关联），11000条点评关联记录（即有11000家饿了么店与点评店铺相关联），3娃0000条百度关联记录（即有30000家饿了么店铺与百度店铺相关联）。至于与其他外卖平台关联数据分布不均是因为点评外卖平台上的店铺数量较多，百度外卖平台上的的店铺数量较少，由于店铺基数少，我们人工抽出来进行关联的店铺便比较少。

### 3.2 数据分析

#### 3.2.1 定义关键词

为了方便我们进行数据分析，定义如下关键词

* 覆盖率：

定义：某一店铺属性在某一外卖平台上所有数据中的存在的比率； 举例：100万的数据中，90条店铺数据的name不为空（name != null && name != "")，则称name属性的覆盖率为90%；子属性等级：低、中、高；子属性介绍：覆盖率分三个子属性，当覆盖率在[0%, 50%]的时候称覆盖率低， 当覆盖率在(50%, 80%]的时候称覆盖率中，当覆盖率在[80%, 100%]的时候，称覆盖率高。

* 长度

定义：某一店铺属性的内容长度；举例：外卖店铺A的name属性值为，“小超家小炒肉”，则这个店铺的name属性长度遍为6；

* 平均长度

定义：某一家外卖平台的所有店铺数据在某一属性上长度的平均值；

#### 3.2.2 分析所有属性

* 覆盖率分析：计算所有属性在某一平台上的覆盖率

经过计算，各个平台属性及其覆盖率如下：

饿了么外卖平台：

|属性名|意义|覆盖率|覆盖率等级|
|:----|:---|:---|:-------|
|eleme_name|饿了么店铺名称|0.9999766668999976|高|
|eleme_branch_name|饿了么分店名称|0.000069999|低|
|eleme_address|饿了么店铺地址|0.9977433558997744|高|
|eleme_phone|饿了么店铺电话|0.995730042699573|高|
|eleme_latitude|饿了么店铺纬度|0.9889467771988947|高|
|eleme_longitude|饿了么店铺经度|0.9889467771988947|高|
|eleme_logo_hash|饿了么店铺url|0.8971910280897191|高|

美团外卖平台：

|属性名|意义|覆盖率|覆盖率等级|
|:----|:---|:---|:-------|
|meituan_name|美团外卖店铺名称|0.9994544925225906|高|
|meituan_branch_name|美团外卖分店名称|0.3305916636282183|低|
|meituan_address|美团外卖店铺地址|0.9997484447383966|高|
|meituan_phone|美团外卖店铺电话|0.9997569241292372|高|
|meituan_latitude|美团外卖店铺纬度|0.9981769309692792|高|
|meituan_longitude|美团外卖店铺经度|0.9997597505928507|高|
|meituan_logo_hash|美团外卖店铺url|0.9985952475840802|高|


点评外卖平台：

|属性名|意义|覆盖率|覆盖率等级|
|:----|:---|:---|:-------|
|dianping_name|点评外卖店铺名称|0.9999950677688559|高|
|dianping_branch_name|点评外卖分店名称|0.2362094817211514|低|
|dianping_address|点评外卖店铺地址|0.9999950677688559|高|
|dianping_phone|点评外卖店铺电话|0.6718315347130428|中|
|dianping_latitude|点评外卖店铺纬度|0.9973785191469213|高|
|dianping_longitude|点评外卖店铺经度|0.9987299504803994|高|
|dianping_logo_hash|点评外卖店铺url|0.894709195651745|高|

百度外卖平台：

|属性名|意义|覆盖率|覆盖率等级|
|:----|:---|:---|:-------|
|baidu_name|百度外卖店铺名称|1.0|高|
|baidu_branch_name|百度外卖分店名称|0.6753078178311823|中|
|baidu_address|百度外卖店铺地址|1.0|高|
|baidu_phone|百度外卖店铺电话|1.0|高|
|baidu_latitude|百度外卖店铺纬度|1.0|高|
|baidu_longitude|百度外卖店铺经度|1.0|高|
|baidu_logo_hash|百度外卖店铺url|0.5942664293131583|中|

* 长度和平均长度分析分析：分析各个属性的长度

因为店铺的url和店铺的分店名称覆盖率比较低，所以排出分析这两个属性；因为店铺电话，店铺经纬度属于数字而不属于字符串，所以没有长度这个特性，也排出分析这三个属性，最终我们分析店铺名称，店铺地址这两个字符串属性的长度和平均长度。

![饿了么外卖平台店铺名称分析](http://oppz2fvil.bkt.clouddn.com/eleme-name-length.png)
![饿了么外卖平台店铺地址分析](http://oppz2fvil.bkt.clouddn.com/eleme-address-length.png)
![点评外卖平台店铺名称分析](http://oppz2fvil.bkt.clouddn.com/dianping-name-length.png)
![点评外卖平台店铺地址分析](http://oppz2fvil.bkt.clouddn.com/dianping-address-length.png)
![美团外卖平台店铺名称分析](http://oppz2fvil.bkt.clouddn.com/meituan-name-length.png)
![美团外卖平台地址名称分析](http://oppz2fvil.bkt.clouddn.com/meituan-address-length.png)
![百度外卖平台店铺名称分析](http://oppz2fvil.bkt.clouddn.com/baidu-name-length.png)
![百度外卖平台店铺名称分析](http://oppz2fvil.bkt.clouddn.com/baidu-address-length.png)

经过上面数据统计可得出如下结论：

* 四家外卖平台上的店铺名称多数在 20 字符以下，大多在 10 字符左右
* 四家外卖平台上的店铺地址多数在 60 字符以下，大多在 20 字符左右

经过计算，各平台各属性的平均长度如下：

|平台|属性|平均长度|
|:--|:--|:------|
|饿了么|name|7.48828511715|
|饿了么|address|14.2344543221|
|美团外卖|name|5.54557248607|
|美团外卖|address|17.1581717303|
|点评外卖|name|6.81305117683|
|点评外卖|address|11.5848023162|
|百度外卖|name|5.37198486871|
|百度外卖|address|17.0260903427|

综合上面两方面分析，可得到，所有平台的店铺名称属性属于较短的字符串，地址属性属于中等长度字符串

* 电话属性分析

经过与公司运营人员的沟通，电话属性属于一致性的强校验，即如果两家虚拟店铺的电话一致，则可以认为两家虚拟店铺的实体店为一家。

* 经纬度属性分析

经过与公司运营人员的沟通，如果两家虚拟店铺的距离在500米之内，并且名称相同，地址相同，则可以认为两家虚拟店铺的相似度较高，如果距离在200米之内，并且名称相同，地址相同，则可以认为两家虚拟店铺的相似度更高，如果距离在100米之内，并且名称相同，地址相同，则可以认为两家虚拟店铺的实体店为一家。

#### 3.3.3 选取关键属性

经过上面的数据分析，我们最终选出下面几个店铺属性作为判断店铺是否重复，计算店铺信息的相似度的关键属性

* 店铺名称
* 店铺地址
* 店铺电话
* 店铺经纬度

### 3.3 选取算法

#### 3.3.1 名称地址数据处理算法

店铺的名称和地址属性都是字符串，其内容更是杂乱无章，和电话字符串，经纬度不同，无法按照一些硬性规律进行匹配分析，只能进行粗暴的字符串匹配。

字符串匹配算法有很多，我们挑选出四个比较适合的算法：Cosine Similar算法，JaroWinkler Similar算法，Levenshtein Similar算法，Longest Common Subsequence算法。我们接下来便是要分析上面这几个算法的表现怎么样。

分析方法如下：

* 取出1万条已经被运营人员判定重复的店铺名称和地址信息作为确定重复的字符串，用每个算法进行字符串匹配得出平均分数
* 取出1万条已经被运营人员判定不重复的店铺名称和地址信息作为确定不重复的字符串，用每个算法进行字符串匹配得出平均分数
* 用 重复的平均分数 减去 不重复的平均分数 得出该算法的匹配分数差值
* 计算差值越大，判定算法表现越好，我们暂称分数差值为 表现度

经过计算，各算法表现结果如下：

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-美团外卖|name|Cosine Similar算法|0.874693910276|
|饿了么-美团外卖|name|JaroWinkler Similar算法|0.895600287938|
|饿了么-美团外卖|name|Longest Common Subsequence算法|0.880229755959|
|饿了么-美团外卖|name|Levenshtein Similar算法|0.85060567604|

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-美团外卖|address|Cosine Similar算法|0.547868348786|
|饿了么-美团外卖|address|JaroWinkler Similar算法|0.453714270955|
|饿了么-美团外卖|address|Longest Common Subsequence算法|0.525965282457|
|饿了么-美团外卖|address|Levenshtein Similar算法|0.45665877405|

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-点评外卖|name|Cosine Similar算法|0.905393302043|
|饿了么-点评外卖|name|JaroWinkler Similar算法|0.910325190996|
|饿了么-点评外卖|name|Longest Common Subsequence算法|0.910325190996|
|饿了么-点评外卖|name|Levenshtein Similar算法|0.884591087615|

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-点评外卖|address|Cosine Similar算法|0.615785308543|
|饿了么-点评外卖|address|JaroWinkler Similar算法|0.490861742733|
|饿了么-点评外卖|address|Longest Common Subsequence算法|0.58537468161|
|饿了么-点评外卖|address|Levenshtein Similar算法|0.520828079438|

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-百度外卖|name|Cosine Similar算法|0.865768076318|
|饿了么-百度外卖|name|JaroWinkler Similar算法|0.89171533505|
|饿了么-百度外卖|name|Longest Common Subsequence算法|0.870285563144|
|饿了么-百度外卖|name|Levenshtein Similar算法|0.836630708777|

|匹配对|属性名|算法名|表现度|
|:----|:----|:----|:----|
|饿了么-百度外卖|address|Cosine Similar算法|0.55251152149|
|饿了么-百度外卖|address|JaroWinkler Similar算法|0.439412462372|
|饿了么-百度外卖|address|Longest Common Subsequence算法|0.523866323238|
|饿了么-百度外卖|address|Levenshtein Similar算法|0.452664365676|

经过上面进行的算法分析，我们得出结论如下：

* 对于name属性而言，综合各种算法的表现程度, JaroWinkler Similar算法在各种匹配对上(饿了么-美团外卖, 饿了么-点评外卖, 饿了么-百度外卖)表现都很好，我们选定在匹配name属性上则使用JaroWinkler Similar算法进行匹配
* 对于address属性而言，纵隔各种算法的表现程度，Cosine Similar算法在各种匹配对上(饿了么-美团外卖, 饿了么-点评外卖, 饿了么-百度外卖)表现都很好，我们选定在匹配address属性上则使用Cosine Similar算法进行匹配

#### 3.3.2 电话数据处理算法

对于电话属性而言，虽然本质是字符串，但有着很强的规律可循。对于电话号码而言，只有两个电话字符串完全相同，才能判定电话号码一致。拿所拥有的电话数据来看，phone（店铺的电话属性）内容可包含多个电话号码，而且电话号码之间的分隔字符也并不是一致的，比如像 "a_b"、"a, b"、"a/b" 、"a b" 等这些分隔符分割多个电话号码。phone属性内容还包含了座机号码，格式大多如 "0412-7777727"、 "04217777727"、"7777727"。

由于电话数据格式不统一，我们定义匹配电话数据算法逻辑（将A店铺电话字符串和B店铺电话字符串进行匹配）如下：

* 将A店铺的phone属性和B店铺的phone属性的内容分隔符统一: 将所有可能出现的分隔符(',', '-', '/', '\\', ' ', '，', '／', '、', '.', '。', '|', '_', '——')全部替换成一致的(如',')
* 将A店铺的phone属性和B店铺的phone属性的内容字符串按照','全部分割开
* 将A店铺的phone属性和B店铺的phone属性分隔之后的电话数据中长度小于7的去除(电话号码最短7位)
* 分别遍历A店铺phone属性分隔之后的电话列表（设置遍历的当前电话phone1)和B店铺phone属性分隔之后的电话列表（设置遍历的当前电话phone2)，如果phone1等于phone2，或者phone1包含phone2，或者phone2包含phone1，都将确认A店铺的电话和B店铺的电话一致。（如 phone1='18804040404'和phone2='18804040404'、phone1='04217751555'和phone2='7751555'、phone1='7751555'和phone2='04217751555' 都算电话一致）
* 如果判定电话属性一致，则判定A店铺和B店铺为同一家实体店铺，否则不一致（电话判定结果只有1.0一致、0.0不一致两个结果）

#### 3.3.3 经纬度距离算法

根据地球上两个店的经纬度，计算球面距离，根据球面距离来计算店铺的相似度。

## 第4章 店铺判重算法实现和优化

### 4.1 店铺判重算法实现

#### 4.1.1 名称地址相似度分数阀值计算

经过上面的算法分析，我们选出JaroWinkler Similar算法对店铺name属性进行匹配，Cosine Similar算法对店铺address进行匹配。 下面，我们分别拿出1万条已经确认重复的店铺信息和1万条已经确认不重复的店铺信息分别进行name和adress属性的匹配，最终定出权重和阀值。数据分析结果如下：

![eleme-baidu:name](http://oppz2fvil.bkt.clouddn.com/eleme-baidu:name-%5BJaroWinklerSimilar%5D.png)
![eleme-baidu:address](http://oppz2fvil.bkt.clouddn.com/eleme-baidu:address-%5BCosineSimilar%5D.png)
![eleme-meituan:name](http://oppz2fvil.bkt.clouddn.com/eleme-meituan:name-%5BJaroWinklerSimilar%5D.png)
![eleme-meituan:address](http://oppz2fvil.bkt.clouddn.com/eleme-meituan:address-%5BCosineSimilar%5D.png)
![eleme-dianping:name](http://oppz2fvil.bkt.clouddn.com/eleme-dianping:name-%5BJaroWinklerSimilar%5D.png)
![eleme-dianping:address](http://oppz2fvil.bkt.clouddn.com/eleme-dianping:address-%5BCosineSimilar%5D.png)

经过数据分析，我们得出结论如下：

* 饿了么和百度外卖平台上店铺名称属性当JaroWinklerSimilar匹配分数在(0.8, 1.0]则可以认为名称一致，匹配分数在(0.6, 0.8]之间可认为名称比较相似，匹配分数在(0.5, 0.6]之间可以认为名称可能相似，匹配分数在[0.0, 0.5]之间可以认为名称不相似。
* 饿了么和百度外卖平台上店铺地址属性当CosineSimilar匹配分数在(0.8, 1.0]则可以认为地址一致，匹配分数在(0.6, 0.8]可以认为极为相似，匹配分数在(0.4, 0.6]之间可认为名称比较相似，匹配分数在(0.3, 0.4]之间可以认为名称可能相似，匹配分数在[0.0, 0.3]之间可以认为名称不相似。
* 饿了么和美团外卖平台上店铺名称属性当JaroWinklerSimilar匹配分数在(0.8, 1.0]则可以认为名称一致，匹配分数在(0.6, 0.8]之间可认为名称比较相似，匹配分数在(0.5, 0.6]之间可以认为名称可能相似，匹配分数在[0.0, 0.5]之间可以认为名称不相似。
* 饿了么和美团外卖平台上店铺地址属性当CosineSimilar匹配分数在(0.8, 1.0]则可以认为地址一致，匹配分数在(0.6, 0.8]可以认为极为相似，匹配分数在(0.4, 0.6]之间可认为名称比较相似，匹配分数在(0.3, 0.4]之间可以认为名称可能相似，匹配分数在[0.0, 0.3]之间可以认为名称不相似。
* 饿了么和点评外卖平台上店铺名称属性当JaroWinklerSimilar匹配分数在(0.8, 1.0]则可以认为名称一致，匹配分数在(0.6, 0.8]之间可认为名称比较相似，匹配分数在(0.5, 0.6]之间可以认为名称可能相似，匹配分数在[0.0, 0.5]之间可以认为名称不相似。
* 饿了么和点评外卖平台上店铺地址属性当CosineSimilar匹配分数在(0.8, 1.0]则可以认为地址一致，匹配分数在(0.6, 0.8]可以认为极为相似，匹配分数在(0.4, 0.6]之间可认为名称比较相似，匹配分数在(0.3, 0.4]之间可以认为名称可能相似，匹配分数在[0.0, 0.3]之间可以认为名称不相似。

最终我们定义如下分数：

* 名称一致 1.0分
* 名称极为相似 0.9分
* 名称比较相似 0.8分
* 名称可能相似0.6分
* 名称不相似0.0分

#### 4.1.2 经纬度距离分数阀值计算

我们在各个平台上选出1万对已经经过人工判定相似的店铺和1万对人工判定不相似的店铺（饿了么店铺-美团外卖店铺，饿了么店铺-百度外卖店铺，饿了么店铺-点评外卖店铺）进行经纬度距离分析，分析结果如下:

![eleme-meituan-distance](http://oppz2fvil.bkt.clouddn.com/eleme-meituan:%5Bspherical-distance%5D.png)
![eleme-dianping-distance](http://oppz2fvil.bkt.clouddn.com/eleme-dianping:%5Bspherical-distance%5D.png)
![eleme-baidu-distance](http://oppz2fvil.bkt.clouddn.com/eleme-baidu:%5Bspherical-distance%5D.png)

上面数据分析条形图横轴：店铺距离（单位100米），纵轴所占比例。图中两种颜色的数据柱，蓝色数据柱为经过判定相似的店铺（饿了么店铺-美团外卖店铺，饿了么店铺-百度外卖店铺，饿了么店铺-点评外卖店铺）的距离分布，橘黄色数据柱为经过判定不相似的店铺的距离分布情况。

经过分析，我们能得出如下结论：

* 在[饿了么-美团外卖]店铺信息对中，确定重复的店铺对中，70%的店铺对距离在[0,200]米之内，15%的店铺对距离在(200,300]米之内，7%的的店铺对距离在(300, 400]米之内，3%的店铺对距离在(400, 500]米之内，其余的店铺对则距离多于500米，比例大概占5%；确定不重复的店铺对中，100%的店铺对距离都超过1000米
* 在[饿了么-点评外卖]店铺信息对中，确定重复的店铺对中，62%的店铺对距离在[0,200]米之内，15%的店铺对距离在(200,300]米之内，8%的的店铺对距离在(300, 400]米之内，6%的店铺对距离在(400, 500]米之内，其余的店铺对则距离多于500米，比例大概占9%；确定不重复的店铺对中，100%的店铺对距离都超过1000米
* 在[饿了么-百度外卖]店铺信息对中，确定重复的店铺对中，3%的店铺对距离在[0,200]米之内，30%的店铺对距离在(200,300]米之内，50%的的店铺对距离在(300, 400]米之内，8%的店铺对距离在(400, 500]米之内，4%的店铺对距离在(500, 600]米之内，其余的店铺对则距离多于600米，比例大概占5%；确定不重复的店铺对中，100%的店铺对距离都超过1000米

经过上面数据分析，我们可以设置如下距离匹配分数：

饿了么店铺-美团外卖店铺：

|距离段|分数段|
|:----|:----|
|[0, 100]|[1.0, 0.9]|
|(100, 200]|(0.9, 0.8]|
|(200, 300]|(0.8, 0.6]|
|(300, 400]|(0.6, 0.5]|
|(400, 1000]|(0.5, 0.0]|
|(1000, +]|0.0|

饿了么店铺-点评外卖店铺：

|距离段|分数段|
|:----|:----|
|[0, 100]|[1.0, 0.9]|
|(100, 200]|(0.9, 0.8]|
|(200, 300]|(0.8, 0.6]|
|(300, 400]|(0.6, 0.5]|
|(400, 1000]|(0.5, 0.0]|
|(1000, +]|0.0|

饿了么店铺-百度外卖店铺：

|距离段|分数段|
|:----|:----|
|[0, 200]|(0.5, 0.3]|
|(200, 300]|(0.9, 0.7]|
|[300, 400]|[1.0, 0.9]|
|(400, 500]|(0.7, 0.5]|
|(500, 1000]|(0.5, 0.0]|
|(1000, +]|0.0|


#### 4.1.3 店铺判重算法整合实现

经过上面的数据分析，我们已经选出可判定重复店铺的关键属性（名称，地址，电话，经纬度），我们也对应着每一种关键属性进行了算法分析、编写、挑选，计算出了最适应该属性的匹配算法，和其在各个平台上独有的阀值，下面我们根据上面的分析，编写出一整套门店判重算法（我们暂定名称权重0.5，地址权重0.3，经纬度距离权重0.3）算法的步骤如下：

1. 初始化数据，拿到一家饿了么店铺A的基本信息a_info， 拿到一家非饿了么平台店铺B的基本信息b_info。
2. 用电话匹配算法对店铺A的电话属性a_phone和店铺B的电话属性b_phone进行匹配，如果分数等于1.0则跳到步骤7，否则跳到步骤3。
3. 用Jarowinkler Similar算法对店铺A的名称属性a_name和店铺B的名称属性b_name进行匹配，根据4.1.1章节的相似度阀值，得出匹配分数name_score，并跳到步骤4。
4. 用Cosine Similar算法对店铺A的地址属性a_address和店铺B的地址属性b_address进行匹配，根据4.1.1章节的相似度阀值，得出地址匹配分数address_score，并跳到步骤5。
5. 用经纬度距离算法和4.1.2章节所计算出的距离分数比对，得出距离分数distance_score，并且跳到步骤6。
6. 根据公式: all_score = name_score*0.5 + address_score*0.3 + distance_score*0.2 得出最终匹配分数 all_score，跳到步骤7。
7. 得出最终匹配分数。

我们根据上面的步骤画出流程图：

![门店判重算法流程图](http://oppz2fvil.bkt.clouddn.com/shop_match_flow_chart.png)

下面是整合之后的代码：

提供的店铺model代码:

```python
class Shop(object):
    ELEME_SOURCE = ELEME_SOURCE
    MEITUAN_SOURCE = MEITUAN_SOURCE
    DIANPING_SOURCE = DIANPING_SOURCE
    BAIDU_SOURCE = BAIDU_SOURCE

    sources = ['eleme', 'meituan', 'dianping', 'baidu']


    def __init__(self, name, address, phones, latitude, longitude, source):
        self.name = name
        self.address = address
        self.phones = phones
        self.latitude = latitude
        self.longitude = longitude
        self.source = source


    def __str__(self):
        return 'name[%s], address[%s], phones[%s], latitude[%s], longitude[%s], source[%s]' % (self.name, self.address, self.phones, self.latitude, self.longitude, self.sources[self.source])


    def match_shop(self, other_shop):
        if self.source == self.ELEME_SOURCE and other_shop.source == self.ELEME_SOURCE or self.source != self.ELEME_SOURCE and other_shop.source != self.ELEME_SOURCE:
            raise Exception ('能且只能进行 饿了么店铺 和 竞对店铺 进行匹配')
        
        eleme_poi_shop = None
        other_poi_shop = None
        other_poi_source = None
        if self.source == self.ELEME_SOURCE:
            eleme_poi_shop = self
            other_poi_shop = other_shop
            other_poi_source = other_poi_shop.source
        elif other_shop.source == self.ELEME_SOURCE:
            eleme_poi_shop = other_shop
            other_poi_shop = self
            other_poi_source = other_poi_shop.source
        else:
            raise Exception ('能且只能进行 饿了么店铺 和 竞对店铺 进行匹配')

        return calc_shop_similar_score(eleme_poi_shop, other_poi_shop, other_poi_source) # 计算两个店铺的匹配度
```

各个算法的阀值配置：

```python
ELEME_SOURCE = 0
MEITUAN_SOURCE = 1
DIANPING_SOURCE = 2
BAIDU_SOURCE = 3

ALL_SOURCES = [
    {
        'pinyin':'eleme',
        'name':u"饿了么",
        'source':ELEME_SOURCE,
    },
    {
        'pinyin':'meituan',
        'name':u"美团外卖",
        'source':MEITUAN_SOURCE,
    },
    {
        'pinyin':'dianping',
        'name':u"点评外卖",
        'source':DIANPING_SOURCE,
    },
    {
        'pinyin':'baidu',
        'name':u"百度外卖",
        'source':BAIDU_SOURCE,
    }
]

# 电话匹配分数阀值 score >= phone_threshold 确认匹配，否则继续进行别属性匹配
phone_threshold = 1.0 

# 店铺各种属性的权重
name_weight = 0.5
address_weight = 0.3
distance_weight = 0.2

# 店铺的名称，地址在匹配分数段上对应的得分
eleme_baidu_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_baidu_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_meituan_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_meituan_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_dianping_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_dianping_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]


# 店铺 经纬度距离 和对应的得分
eleme_meituan_distance = [
    {
        'max_distance':100,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':0,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.8,
        'min_distance':100,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.6,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.8,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':300,
        'min_include':False,
        'return_min_score':0.6,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]

eleme_dianping_distance = [
    {
        'max_distance':100,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':0,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.8,
        'min_distance':100,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.6,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.8,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':300,
        'min_include':False,
        'return_min_score':0.6,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]

eleme_baidu_distance = [
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.3,
        'min_distance':0,
        'min_include':True,
        'return_min_score':0.5,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.7,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':300,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':500,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.7,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':500,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]
```

主要店铺判重逻辑代码：

```python
def calc_shop_similar_score(eleme_shop, other_shop, other_source):
    ps = PhoneSimilar(eleme_shop.phones, other_shop.phones)
    phone_score = ps.calc_similar() # 使用 电话匹配度 算法

    if phone_score >= phone_threshold:
        return phone_score
    else:
        name_score = calc_shop_name_similar(eleme_shop.name, other_shop.name, other_source)
        address_score = calc_shop_address_similar(eleme_shop.address, other_shop.address, other_source)
        distance_score = calc_shop_distance_similar(eleme_shop.latitude, eleme_shop.longitude, other_shop.latitude, other_shop.longitude, other_source)
        print 'name[%s], address[%s]. distance[%s]' % (name_score, address_score, distance_score)

        return name_score*name_weight + address_score*address_weight + distance_score*distance_weight


def calc_shop_name_similar(eleme_name, other_name, other_source):
    jw = JaroWinklerSimilar(eleme_name, other_name)
    similar_score = jw.jarowinkler_similar() # 使用 JaroWinkler 相似度算法

    one_source = ALL_SOURCES[other_source]
    
    return get_smc_name_score(similar_score, one_source) # 获取经过阀值重新计算之后的名称分数


def calc_shop_address_similar(eleme_address, other_address, other_source):
    cs = CosineSimilar(eleme_address, other_address)
    similar_score = cs.calc_similar() # 使用 CosineSimilar 相似度算法

    one_source = ALL_SOURCES[other_source]

    return get_smc_address_score(similar_score, one_source) # 获取经过阀值重新计算之后的地址分数


def calc_shop_distance_similar(eleme_lat, eleme_lnt, other_lat, other_lnt, other_source):
    sd = SphericalDistance(eleme_lnt, eleme_lat, other_lnt, other_lat)
    distance = sd.calc_distance() # 计算 两点球面距离

    one_source = ALL_SOURCES[other_source]

    return get_smc_distance_score(distance, one_source) # 获取经过阀值重新计算之后的距离分数


def get_smc_name_score(similar_score, one_source):
    score_step =  eval('eleme_%s_name' % one_source['pinyin'])
    for one_step in score_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_score'], '>=' if one_step['max_include'] else '>', similar_score, one_step['min_score'], '<=' if one_step['min_include'] else '<', similar_score)
        if eval(condition):
            return one_step['return_score']


def get_smc_address_score(similar_score, one_source):
    score_step =  eval('eleme_%s_address' % one_source['pinyin'])
    for one_step in score_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_score'], '>=' if one_step['max_include'] else '>', similar_score, one_step['min_score'], '<=' if one_step['min_include'] else '<', similar_score)
        if eval(condition):
            return one_step['return_score']


def get_smc_distance_score(distance, one_source):
    distance_step = eval('eleme_%s_distance' % one_source['pinyin'])
    for one_step in distance_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_distance'], '>=' if one_step['max_include'] else '>', distance, one_step['min_distance'], '<=' if one_step['min_include'] else '<', distance)
        if eval(condition):
            step_distance = one_step['max_distance'] - one_step['min_distance']
            step_score = one_step['return_min_score'] - one_step['return_max_score']
            distance_ratio = (distance - one_step['max_distance']) * 1.0 / step_distance
            return one_step['return_min_score'] - distance_ratio * step_score 

```

### 4.2 店铺判重算法优化

### 4.3 店铺判重算法打包

### 4.3.1 打Python包

## 结论

## 参考文献

## 致谢
