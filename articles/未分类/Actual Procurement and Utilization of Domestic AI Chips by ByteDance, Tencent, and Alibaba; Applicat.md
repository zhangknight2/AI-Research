---
title: "Actual Procurement and Utilization of Domestic AI Chips by ByteDance, Tencent, and Alibaba; Application Prospects and Rollout Pace of Domestic Chips in Generative AI Inference; Opportunities in Domestic Interconnect Chips, Advanced Packaging, etc. – Ascend/Cambricon/Hygon/Synlight/JCET Group Co., Ltd."
source: "https://www.acecamptech.com/article/detail/70559852"
category: "未分类"
date: "2026/03/16 Mon 06:00"
downloaded: "2026-03-22 20:15:32 JST"
---

# Actual Procurement and Utilization of Domestic AI Chips by ByteDance, Tencent, and Alibaba; Application Prospects and Rollout Pace of Domestic Chips in Generative AI Inference; Opportunities in Domestic Interconnect Chips, Advanced Packaging, etc. – Ascend/Cambricon/Hygon/Synlight/JCET Group Co., Ltd.

Actual Procurement and Utilization of Domestic AI Chips by ByteDance, Tencent, and Alibaba; Application Prospects and Rollout Pace of Domestic Chips in Generative AI Inference; Opportunities in Domestic Interconnect Chips, Advanced Packaging, etc. – Ascend/Cambricon/Hygon/Synlight/JCET Group Co., Ltd.

Expert 1-on-1

Chinese

EN

The original version is in Chinese FYI

Actual Procurement and Utilization of Domestic AI Chips by ByteDance, Tencent, and Alibaba; Application Prospects and Rollout Pace of Domestic Chips in Generative AI Inference; Opportunities in Domestic Interconnect Chips, Advanced Packaging, etc. – Ascend/Cambricon/Hygon/Synlight/JCET Group Co., Ltd.

VIPOriginalIndustry：Semiconductor

2026/03/17 23:56:51

Views 9377

Likes 1

Quick-Q

Summary

Key points of this article include:
1. Actual procurement and utilization of domestic AI chips by ByteDance, Tencent, and Alibaba
2. Application prospects and rollout pace of domestic chips in generative AI inference
3. Changes in the competitive landscape of the domestic AI accelerator card market
4. Opportunities in domestic interconnect chips and advanced packaging.

The full text is 3108 words, estimated reading time 7 minutes

VIP Free

Below are expert opinions:

**1. Against the backdrop of current domestic compute power shortages, what is the actual procurement and utilization of domestic AI chips by CSPs (such as ByteDance, Tencent, Alibaba)?**

Domestic CSPs have complex businesses that are already deployed at scale, resulting in enormous demand for compute power, which is still primarily met by NVIDIA. Although Amazon's Trainium and Google's TPU are alternative inference chips, their compute rental is irrelevant to domestic companies. Even if domestic compute power offers decent performance, its production capacity is a drop in the bucket and cannot meet the needs of large-scale inference. Companies such as Alibaba and ByteDance purchase and deploy a certain quantity of domestic chips, mainly to fulfill some administrative requirements. However, domestic chip manufacturers like Cambricon must also prioritize other government orders and intelligent computing center projects, making it impossible to allocate all capacity to a single client. Therefore, in reality, the supply of domestic chips is extremely limited.

**2. How is ByteDance currently using domestic chips such as Cambricon? If SMIC's capacity increases in the future and domestic chip supply rises, can market demand absorb it?**

Currently, ByteDance mainly uses domestic chips such as Cambricon for inference in traditional businesses, rather than for generative AI inference related to LLMs. These traditional businesses primarily involve image and speech recognition and recommendation systems based on convolutional and recurrent neural networks, such as content safety review (identifying pornographic, violent, or terrorist content) and complex user behavior analysis. These algorithms happen to be areas where early domestic chip architectures excel. For generative AI, which requires strong attention operator capabilities and high memory bandwidth, domestic chips face hardware limitations. ByteDance also develops dedicated chips (such as transcoding chips) internally to offload some traditional AI processing tasks. As a result, incremental demand for domestic chips in traditional businesses is limited and may not even grow. Even if domestic chip capacity increases in the future, there will not be an oversupply, as current demand is not fully met.

**3. Looking ahead, what are the application prospects and rollout pace for domestic chips in generative AI inference? How will ByteDance's domestic inference compute deployment evolve?**

With ongoing adaptation efforts and continuous iterations of domestic chips (such as Ascend, Cambricon, Hygon), there is potential for application in generative AI inference in the future. However, at present, ByteDance's subsequent inference compute may become increasingly reliant on its data centers in Southeast Asia. Domestically, the pace of deploying inference using domestic chips or resource cards remains unclear. At this stage, domestic chips are mainly used to meet policy requirements and handle traditional AI workloads, with no significant advantage in performance or cost. Achieving large-scale application in generative AI inference will require further iterations in domestic manufacturing processes and overall performance improvements; this process is expected to be gradual, with no fundamental changes likely in the short term.

**4. What are the trends in next-generation product architectures among domestic AI chip manufacturers? What are their main application scenarios and commercialization strategies?**

Currently, leading domestic AI chip manufacturers generally favor inference over training in their next-generation product architectures. Only a few, such as Hygon, Cambricon, Baidu Kunlun, Enflame, and Iluvatar CoreX, retain some focus on training. The industry has seen the emergence of a "P-D separation" paradigm, featuring two core designs: Prefill, dedicated to inference and also applicable to recommendation systems; and Decode, which, in addition to handling decoding tasks, structurally resembles training chips and can also support training needs. Nevertheless, in practice, few clients use these domestic chips for large-scale training, a domain still dominated by Huawei's products due to their higher compute density.

Manufacturers generally believe that focusing on the inference market enables faster commercialization. As a result, companies like Moore Threads and Muxi are actively developing inference appliances in desktop workstation or server form factors. These products mainly target SMEs or verticals such as government, healthcare, and legal, meeting their needs for data security in privatized, closed deployments. These scenarios have relatively low compute requirements and represent promising entry points for domestic compute power.

In contrast, although some domestic data center-level compute projects have been built, their application results are generally unsatisfactory, lacking effective commercial use cases, with some projects (such as "City Brain") still at the conceptual stage. Therefore, the mainstream industry strategy has shifted from directly competing with NVIDIA in large data centers to a more pragmatic, commercialization-driven approach, prioritizing the rollout of inference products.

**5. What is the division of labor and cooperation model between chip design companies and large system solution providers in the domestic compute power industry ecosystem?**

A clear division of labor has now taken shape in the domestic compute power industry: large operators and system solution providers (such as Sugon and Inspur) are responsible for addressing interconnection issues in large clusters, building hybrid compute clusters compatible with multi-vendor GPUs and ASICs, and driving overall development at the national compute center level.

Chip design companies, on the other hand, focus on developing their respective chip products, ensuring smooth integration into the software stacks and hardware systems of these heterogeneous large clusters. Under this division of labor, chip design companies can concentrate more on commercialization strategies and market development. The new generation of domestic AI chips is designed with flexibility in mind, supporting both large-scale networked applications with thousands of cards and smaller workstation-level applications with multiple cards per machine, though the market focus remains on small-scale systems.

**6. How should we view the competitive landscape of the domestic AI accelerator card market? How do the technical routes and foundry strategies of major manufacturers differ?**

Currently, Huawei Ascend holds a clear leading position in the domestic AI accelerator card market, followed by Cambricon and Hygon, both of which have relatively stable capacity at SMIC and are expected to ramp up in 2026.

Other manufacturers are pursuing diversified development paths:

Moore Threads and Muxi have product architectures similar to NVIDIA and AMD, offering inherent ecosystem advantages and good software compatibility. They adopt a dual-track strategy: on one hand, leveraging mature SMIC processes for product exploration and prototyping; on the other, actively seeking cooperation with Samsung to produce next-generation products, which may match the early models of NVIDIA's Hopper architecture in performance. Although this path is challenging, success would have a positive impact on the entire domestic chip industry chain.

Biren Technology has chosen to partner with HUA HONG SEMI, planning to use its 7nm process for production and serving as a lead customer to assist with process debugging. Biren's product architecture is relatively advanced, with outstanding single-card performance and competitive software capabilities, potentially making it a significant market variable.

Overall, the future market landscape may become more segmented. Manufacturers such as Biren, Moore Threads, and Muxi, which adopt GPU-like architectures, may have greater advantages in next-generation product competition due to their flexibility and potential. In contrast, companies like Cambricon, Hygon, and Baidu Kunlun, whose current product architectures are more ASIC-oriented, would face significant technical and cost challenges if they were to transition to GPU architectures, making such a shift difficult in the short term.

**7. How should we view the future supply-demand relationship in the domestic AI compute market?**

It is expected that for a considerable period, the domestic AI compute market may face insufficient demand. This does not refer to overcapacity, but rather a lack of effective demand. The main reason is that the overall architecture evolution of domestic compute platforms is relatively slow and cannot yet adapt well to mainstream inference business scenarios. Currently, mainstream inference workloads are still concentrated among CSPs, and model companies, due to their needs for training and inference iteration, prefer to use NVIDIA GPUs. As a result, buyers are less willing to procure domestic platforms that are still immature and poorly adapted.

Although foundries such as SMIC have released some capacity, expansion is not unlimited, and capacity allocation is still order-driven. Chip manufacturers have become very pragmatic, typically placing orders with foundries only after securing clear customer orders, in order to avoid significant capital occupation and inventory risks. Therefore, market supply will be adjusted based on actual orders, rather than blind production.

**8. What is the demand situation in the domestic interconnect chip market?**

Unlike the AI compute chip market, which may face insufficient demand, domestic demand for high-performance interconnect chips is very strong, with growth even outpacing GPUs. Many companies, including ByteDance, Alibaba, Tencent, Sugon, and Inspur, are developing their own proprietary interconnect protocols and actively deploying Ethernet-based scale-up switches, driving huge demand for domestic high-performance switch chips. Currently, the supply of domestic switch chips is severely inadequate, and the market outlook is optimistic. Therefore, new advanced process capacity upstream will not be limited to AI compute, as interconnect chips will be another important growth driver.

**9. What is the current status of domestic advanced packaging (such as CoWoS) capacity and development? Can it meet the needs of AI chips?**

The domestic advanced packaging industry is developing in tandem with leading chip design companies. JCET Group Co., Ltd., Synlight, and Huawei's in-house packaging systems are all actively advancing related technologies, including CoWoS and HBM. Although there is still a gap compared to the international cutting edge, it is smaller than that in semiconductor manufacturing processes; for example, domestic progress in 3D DRAM stacking is even faster.

Currently, domestic packaging and testing capacity mainly serves the edge AI market, such as wearables, edge computing, and in-vehicle computing, which are high-volume sectors. High-end packaging demand and capacity for data center-level applications are relatively small, mainly supporting flagship product R&D and limited production for leading companies, and are not yet ready for large-scale ramp-up.

Specifically for CoWoS capacity, apart from Huawei's system, Synlight and JCET Group Co., Ltd. are the main suppliers, and their annual capacity is basically in line with the current annual shipment volume of tens of thousands of domestic high-end AI chips (excluding Huawei). Packaging and testing manufacturers will expand capacity in response to downstream AI chip demand growth, rather than proactively over-investing. Therefore, current packaging capacity can meet the needs of existing domestic AI chips and will gradually increase as the market grows.

Follow-up

[If CSPs like ByteDance shift inference workloads to Southeast Asia, will the valuation logic for Cambricon and Hygon face a de-rating due to insufficient domestic demand?](/chat?title=If%20CSPs%20like%20ByteDance%20shift%20inference%20workloads%20to%20Southeast%20Asia,%20will%20the%20valuation%20logic%20for%20Cambricon%20and%20Hygon%20face%20a%20de-rating%20due%20to%20insufficient%20domestic%20demand?) [With domestic interconnect chip demand outpacing GPUs, can SJ Semiconductor and JCET's advanced packaging capacity expansion capture this structural growth and drive earnings beats?](/chat?title=With%20domestic%20interconnect%20chip%20demand%20outpacing%20GPUs,%20can%20SJ%20Semiconductor%20and%20JCET's%20advanced%20packaging%20capacity%20expansion%20capture%20this%20structural%20growth%20and%20drive%20earnings%20beats?)

ASICGPUCSP

1

Dislikes

Favorite

Share

Expert Bio：

某头部EDA-业务经理

Expert 1-on-1

[![](https://image.acecamptech.com/avatar/50503746/0.23478007761692687.jpg?x-oss-process=style/avatar)](/organizer/20505798)

[Jay Dong](/organizer/20505798)

Acecamp analyst

Follow

执行董事，TMT行业分析师，具有多年美国中概股及港股研究经验，重点关注AI软件及AI应用。
移动电话：18513916796；微信ID：Jinlong\_D

Solemn statement: The above content is based on public information, only represents personal or guests' views. It does not represent any position of AceCamp, any companies, any institutions. The volatility of the stock market is related to many factors. Investment decisions are made by individuals based on their own research and analysis. The purpose of this article or event is the sharing of facts and views and does not constitute any investment suggestions. This article or event content must not be forwarded, reproduced, duplicated, published, modified, or quoted in whole or in part by any institution or individual in any form without the permission of AceCamp and the author. The above content is exclusive to paying clients, and all institutions and individuals are strictly bound by confidentiality obligations and intellectual property agreements. AceCamp is not responsible for the impact of any third party's unauthorized acts while maintaining the rights for legal actions.

Related Recommendations

[![](https://image.acecamptech.com/generates/20260310/29e407ad9c4b.png)

AI Inference Chip Market Supply-Demand Dynamics and Competitive Landscape, Domestic CoWoS Packaging Progress

2026/03/16 Mon 06:00 Event](/eventDetail/60532730)[Domestic AI Chip Channel Check: Impact of Foundry, Packaging, and HBM on Ascend and Cambricon

Key points of this article include:
1. 950 customer test feedback and corresponding mass production ramp-up schedule
2. Uncertainties in upstream mass production for Ascend and Cambricon

2026/03/18 07:31Note](/article/detail/70559931)[Channel Check on Leading Integrated Circuit Manufacturers: Current Capacity and Customer Structure for MOS/BCD/Nor/MCU, Capacity Expansion Pace and Major Client Demand, Price Increase Trends and Company Pricing Strategies—Focus on NVIDIA/MPS/Infineon/SGMICRO/XINJIENERGY/GigaDevice/ST, etc.

1. Current capacity and customer structure for MOS/BCD/Nor/MCU;
2. Capacity expansion pace and major client demand;
3. Price increase trends and company pricing strategies.

2026/03/18 07:23Note](/article/detail/70559929)[Estimates of 2026 Shipments and Product Mix for Ascend, Cambricon, Hygon, etc.; Considerations by ByteDance, Alibaba, etc. for Self-Developed Chips, Ascend, and Overseas Accelerators in Inference Scenarios; Specific Applications of Supernode Products

Key points of this article include:
1. Shipment and product mix estimates for Ascend, Cambricon, Hygon, etc. in 2026
2. Specific considerations by ByteDance and Alibaba regarding the use of self-developed chips, Ascend, and overseas chips in inference scenarios
3. Specific usage of supernode products in China

2026/03/22 04:16Note](/article/detail/70559897)

[Research on Domestic AI Chips: Differences in AI Inference Computing Power Demand Among Major Players Such as ByteDance, Alibaba, and Tencent; 2026 CSP In-house Card Scale Estimates and Comparison with Ascend, Cambricon, etc. in Terms of Capacity Stability; Impact of Packaging, HBM, and Other Constraints – ByteDance/Alibaba/Tencent/Ascend/Cambricon

Key points of this article include:
1. Differences in AI inference computing power demand among major players such as ByteDance, Alibaba, and Tencent
2. Feasibility analysis of using Southeast Asian data centers to address domestic inference computing power demand
3. 2026 scale estimates of in-house cards for ByteDance, Alibaba, Tencent, and Baidu, and comparison with Ascend, Cambricon, etc. in terms of capacity stability
4. Constraints on domestic chips from packaging, HBM, etc.

2026/03/19 01:26Note](/article/detail/70559896)[![](https://image.acecamptech.com/generates/20260316/89266fd7ba6f.png)

Expert call: Qwen Enterprise Agent Updates, Token Hub Strategy Outlook, Compute Demand, etc.

2026/03/19 Thur 06:45 Event](/eventDetail/60532914)[![](https://image.acecamptech.com/generates/20260318/30c8ded898a9.png)

ByteDance In-house Chip Development Channel Check: Performance, Mass Production Plan, Uncertainties, Key Application Areas

2026/03/24 Tues 11:30 Event](/eventDetail/60532969)[![](https://image.acecamptech.com/generates/20260318/f85215ce07de.png)

Domestic AI Chip: Upstream Advanced Process Capacity Expansion Expectations, Changes in Domestic Computing Power Demand and Supply Landscape

2026/03/24 Tues 05:00 Event](/eventDetail/60532962)

[Domestic AI Inference Chip Channel Check: Changes in Inference AI Computing Power Demand from ByteDance, Alibaba, Tencent and Other Leading Companies Since 2026, Annual Shipment Estimates for Ascend 950 and Cambricon 690, and Core Application Directions

Key points of this article include:
1. Changes in inference AI computing power demand from leading domestic companies such as ByteDance, Alibaba, and Tencent since 2026
2. Shipment estimates for Ascend, Cambricon and other vendors in 2026 and core application directions for next-generation products

2026/03/15 04:20Note](/article/detail/70559705)[![](https://image.acecamptech.com/generates/20260318/7790c08b83f9.png)

Volcano Channel Check: Changes in Inference Demand for Doubao and SeeDance, Procurement Expectations for Ascend 950 and Cambricon 690

2026/03/23 Mon 11:00 Event](/eventDetail/60532952)[![](https://image.acecamptech.com/generates/20260311/15be42a99959.png)

Domestic Advanced Process Capacity Expansion Expectations, Changes in Reliance on Samsung and Others, CoWoS Packaging Progress

2026/03/17 Tues 06:00 Event](/eventDetail/60532758)[SeeDance Model Development Plan, Inference Compute Power Supplement Solutions, Domestic H200 Procurement Progress and Domestic Chip Availability, AIDC Expansion Plan

1. SeeDance model development plan and solutions for insufficient compute power
2. Progress of domestic H200 procurement and availability of domestic chips
3. AIDC expansion plan

2026/03/13 08:26Note](/article/detail/70559785)

[Domestic AI Chips and Industry Chain: Exponential Growth in AI Inference Demand, Focus on Leading Foundry Advanced Process Expansion Plans and Market Share Allocation - Ascend/Cambricon/SG Micro

Against the backdrop where the gap in LLM capabilities between China and the US cannot be significantly widened, domestic LLMs, with their lower inference costs, are expected to dominate global AI inference markets in terms of token calls, thereby driving the development of domestic AI chips and the related industry chain.

2026/03/10 01:09Insight](/article/detail/70559603)[ByteDance Channel Check: OpenClaw-like Agent Applications Drive Token Usage, Upward Revision of 2026 Compute CAPEX, In-house Chip R&D Progress and Mass Production Timeline, Domestic Chip Procurement Plans, Storage Supply Expected to Remain Tight Throughout the Year - Focus on Cambricon/NVIDIA/AMD/Hygon/Enflame/Verisilicon/Broadcom

- Market impact and commercialization path of OpenClaw;
- Breakdown of 2026 GPU procurement shares for NVIDIA, AMD, Cambricon, etc.;
- Supply-demand landscape and price outlook for CPU and storage.

2026/03/12 06:26Note](/article/detail/70559729)[AI Chip Testing Channel Check: Comparison Between Domestic and Overseas Test Platforms – Ascend/Cambricon/Hygon/Changchuan Technology/Teradyne/Advantest

1. Cost structure of test platforms 2. Comparison between domestic and overseas test platforms

2026/03/11 03:11Note](/article/detail/70559675)[Domestic Chip Channel Check: Internet Giants' ASIC Demand Characteristics, Comparison of Ascend, 690, etc., and Supply Landscape Expectations for Domestic Chips in 2026 and 2027 – Ascend/Hygon/Kunlunxin/Pingtouge

1. Characteristics of ASIC demand from domestic internet giants; comparison of domestic computing chips
2. Supply landscape expectations for domestic chips in 2026 and 2027
3. DeepSeek V4 outlook

2026/03/10 08:49Note](/article/detail/70559650)

- 1
- 2
- 3
- 4

Comments

Published

![No Data](https://static.acecamptech.com/system/empty.svg)

No Data

Publisher

[![](https://image.acecamptech.com/avatar/50503746/0.23478007761692687.jpg?x-oss-process=style/avatar)](/organizer/20505798)

[Jay Dong](/organizer/20505798)

Published 1107 Articles

Follow

Latest update

[More>](/organizer/20505798)

- [Estimates of 2026 Shipments and Product Mix for Ascend, Cambricon, Hygon, etc.; Considerations by ByteDance, Alibaba, etc. for Self-Developed Chips, Ascend, and Overseas Accelerators in Inference Scenarios; Specific Applications of Supernode Products

  2026/03/22 04:16](/article/detail/70559897)
- [AIDC Channel Check-2: 2026 Domestic and Southeast Asia Deployment Plans of ByteDance, Alibaba, Tencent; Changes in Training and Inference Demand; Progress of Domestic GPU Adoption; Rack Rate Performance by Region – 21Vianet/Range Intelligent Computing Technology Group/Qinhuai Data

  2026/03/20 01:33](/article/detail/70559968)
- [Tencent Channel Check: Time Window for Major Tech Firms to Catch Up with MiniMax and Kimi in Agent Models and Coding, Impact of Model Distillation and Talent on Model Catch-up, and Divergent Effects of OpenClaw on Model Vendors and Cloud Providers – MiniMax/Kimi/Knowledge Atlas/Alibaba/ByteDance

  2026/03/20 01:33](/article/detail/70559895)

![img](https://static.acecamptech.com/system/posters/en_article_poster.png)

Related Radars

[Hot Radars >](/radars)

- [总结最近1个月专家对存储行业的观点，争议和共识，投资机会和风险

  已关注雷达](/radars?monitor_id=c59d4783-4c4e-5c92-b477-95b44c579834)
- 国产 GPU 各公司出货量追踪

  +My Radars
- 阿里巴巴收入及利润预期

  +My Radars
- 阿里云 AI 算力基础设施

  +My Radars
- 下一季各CSP的CapEX预测

  +My Radars
- AI 现在有泡沫吗

  +My Radars

Recent Event

Change

- [![](https://image.acecamptech.com/generates/20260322/ad83fc442381.png)

  Update on Overseas Market Demand Growth for Balcony Solar-plus-Storage Systems

  Active2026/03/24 Tues 11:00](/eventDetail/60533049)
- [![](https://image.acecamptech.com/generates/20260321/42463f8f6583.png)

  Chinese Mainland Power Semiconductor Channel Check: Rectifier/Diode/MOS Supply-Demand and Cost Dynamics, Outlook on Price Hike Potential, Price Transmission Path, and Bottoming Out of SiC and IGBT Prices

  Active2026/03/25 Wed 11:00](/eventDetail/60533045)
- [![](https://image.acecamptech.com/generates/20260320/37f96fd7087f.png)

  Interpretation of Humanoid Robot Motion Capture Equipment

  Active2026/04/07 Tues 12:00](/eventDetail/60533039)
- [![](https://image.acecamptech.com/generates/20260320/d1287c92dbae.png)

  Power Supply Channel Check: Progress in Three-Side Power and Vertical Power Supply, Evolution of PSU/Power Shelf/HVDC Architectures, and Supply Chain Changes Including Megmeet

  Active2026/03/24 Tues 11:00](/eventDetail/60533029)
- [![](https://image.acecamptech.com/generates/20260320/94b0e654894d.png)

  [Company NDR] SenseTime (0020 HK) Post-FY25 Earnings Management Call

  Active2026/03/30 Mon 07:00](/eventDetail/60533024)

For You

- [Channel Check on Liquid Metal and TIM Materials: Transition from GB300 Gallium-Based to Rubin Indium-Based, TIM1/TIM2 Hierarchy Definition, Per-Card Value and Incremental Estimates for Cold Plate Supporting Materials, Customer Adoption, Market Share Landscape, and New Material Roadmap – Focus on NVIDIA/Foxconn/Boyd/Indium Corporation/Fironda/Sinopec

  Note2026/03/21 12:25](/article/detail/70560044)
- [Comparative Analysis of Major US Energy Storage Companies—Tesla/FLNC/Sungrow

  Insight2026/03/21 02:00](/article/detail/70560037)
- [Agentic AI's Compute Explosion Is Real—But Value Only Belongs to Those Who Define the Architecture [GTC/OFC 2026 Series]

  Insight2026/03/21 00:26](/article/detail/70560022)
- [Google TPU Power Supply Channel Check: V7 5.5kW Sample Validation, Upgrade from 5.5kW to 8.5kW, Comparison of Navitas/Infineon Solutions, Delta as Primary Supplier and Share Allocation for Secondary/Tertiary Suppliers, 2026 Market Size Estimate – Focus on Delta, Lite-On, Quanta, Navitas Semiconductor, Infineon, Google, NVIDIA

  Note2026/03/20 10:26](/article/detail/70560025)
- [Update on Leading Forestry Carbon Sink Companies—Business Model, Project Development, and Cooperation Status

  Note2026/03/20 07:26](/article/detail/70560009)

- 1
- 2
- 3
- 4

What’s Hot

Change

- [Estimates of 2026 Shipments and Product Mix for Ascend, Cambricon, Hygon, etc.; Considerations by ByteDance, Alibaba, etc. for Self-Developed Chips, Ascend, and Overseas Accelerators in Inference Scenarios; Specific Applications of Supernode Products

  Note2026/03/22 04:16](/article/detail/70559897)
- [Pfizer Series Report I: Rapid Advancement of PD-1/VEGF Bispecific Pipeline—Combining Speed, Breadth, and Differentiation

  Insight2026/03/22 04:33](/article/detail/70560048)
- [The Iran War: Not Worth Fighting, Too Costly to Quit

  Insight2026/03/22 01:39](/article/detail/70560046)
- [Lithium Carbonate Price Outlook for 2026Q2—Impact of Zimbabwe and Progress of Mica Mine Resumption

  Note2026/03/22 01:35](/article/detail/70560047)
- [Qifu Technology (QFIN): Under Tight Fintech Regulation, Rapid Loan Rate Compression Leads to Sharply Lower Profit Expectations—When Will the Stock Price Inflection Point Arrive?

  Insight2026/03/21 14:32](/article/detail/70559991)

![logo](https://static.acecamptech.com/system/app/app_logo.svg)APP Download

Android & iOS

![wxchat-official](https://static.acecamptech.com/www/static/png/wxchat-official-DRqP0C4T.png)

![logo](data:image/svg+xml,%3csvg%20width='20'%20height='20'%20viewBox='0%200%2020%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='20'%20height='20'%20rx='4'%20fill='%2304CD65'/%3e%3cpath%20d='M12.8315%207.93333C13.015%207.93333%2013.1967%207.94677%2013.3768%207.96677C12.8868%205.69093%2010.4474%204%207.66297%204C4.55%204%202%206.11644%202%208.80395C2%2010.3552%202.84837%2011.6291%204.26605%2012.6172L3.69965%2014.3164L5.67932%2013.3262C6.38769%2013.4661%206.95603%2013.6098%207.66296%2013.6098C7.84066%2013.6098%208.01687%2013.6011%208.19161%2013.5874C8.08097%2013.2097%208.01687%2012.8142%208.01687%2012.4038C8.01688%209.93603%2010.1415%207.93333%2012.8315%207.93333ZM9.78657%206.40184C10.213%206.40184%2010.4954%206.68164%2010.4954%207.1067C10.4954%207.53005%2010.213%207.81375%209.78657%207.81375C9.36213%207.81375%208.93624%207.53005%208.93624%207.1067C8.93624%206.68162%209.36213%206.40184%209.78657%206.40184ZM5.82327%207.81373C5.39888%207.81373%204.97052%207.53003%204.97052%207.10667C4.97052%206.68162%205.39886%206.40182%205.82327%206.40182C6.24769%206.40182%206.53018%206.68162%206.53018%207.10667C6.53018%207.53003%206.24769%207.81373%205.82327%207.81373ZM18%2012.3359C18%2010.0776%2015.7344%208.23682%2013.1898%208.23682C10.4954%208.23682%208.3733%2010.0776%208.3733%2012.3359C8.3733%2014.5981%2010.4954%2016.435%2013.1898%2016.435C13.7538%2016.435%2014.3226%2016.2932%2014.889%2016.1516L16.4423%2017L16.0164%2015.5884C17.1531%2014.7378%2018%2013.6098%2018%2012.3359ZM11.6282%2011.6291C11.3462%2011.6291%2011.0618%2011.3493%2011.0618%2011.0639C11.0618%2010.7825%2011.3462%2010.499%2011.6282%2010.499C12.0565%2010.499%2012.337%2010.7825%2012.337%2011.0639C12.337%2011.3493%2012.0565%2011.6291%2011.6282%2011.6291ZM14.7431%2011.6291C14.4631%2011.6291%2014.1806%2011.3493%2014.1806%2011.0639C14.1806%2010.7825%2014.4631%2010.499%2014.7431%2010.499C15.1675%2010.499%2015.4519%2010.7825%2015.4519%2011.0639C15.4519%2011.3493%2015.1676%2011.6291%2014.7431%2011.6291Z'%20fill='white'/%3e%3c/svg%3e)WeChat Official Account

AceCampTech

Corporate Address

Beijing:307 S3-M26, 3/F, Hopson Place Office Tower, No.A22 Xidawang Road, Chaoyang District, Beijing, China

Hong Kong:66/F, The Center, 99 Queen’s Road Central, Hong Kong

TEL

+86 10 53322308

+852 69069737

Email

[support@acecamptech.com](mailto:support@acecamptech.com)

Copyright©2026 AceCampTech.com. All Rights Reserved.

[Terms of Service](https://terms.acecamptech.com/agreement/index.html)[Privacy Agreement](https://terms.acecamptech.com/privacy/20240120/index.html)

[京ICP备2025158098号-1](https://beian.miit.gov.cn/#/Integrated/index)[京公网安备 11010502043336号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502043336)
