---
title: "Optical Connectivity Expert Interview – Key Discussions from GTC and OFC Tech Events: CPO, Feynman Architecture, Memory Pooling, and OCS"
source: "https://www.acecamptech.com/article/detail/70559948"
category: "未分类"
date: "2026/03/18 Wed 12:00"
downloaded: "2026-03-22 20:15:06 JST"
---

# Optical Connectivity Expert Interview – Key Discussions from GTC and OFC Tech Events: CPO, Feynman Architecture, Memory Pooling, and OCS

Optical Connectivity Expert Interview – Key Discussions from GTC and OFC Tech Events: CPO, Feynman Architecture, Memory Pooling, and OCS

Expert 1-on-1

Chinese

EN

The original version is in Chinese FYI

Optical Connectivity Expert Interview – Key Discussions from GTC and OFC Tech Events: CPO, Feynman Architecture, Memory Pooling, and OCS

VIPOriginalIndustry：​Manufacturing

2026/03/19 02:24:13

Views 13028

Likes 2

Quick-Q

Summary

NVL72 rack updates in HBM and CPU, and NVL576 expansion interconnect solutions.
Core changes in LPU racks, connection methods between GPU and LPU racks.
BlueField memory rack solution, DPU chips.
Google's memory pooling solution, OCS development, and Lumentum's major OCS orders.

The full text is 3252 words, estimated reading time 7 minutes

VIP Free

**The following content is expert sharing for reference only and does not constitute any investment advice.**

\*\* Q&A\*\*

**What are the main changes in NVIDIA's NVL72 rack regarding HBM and CPU, and what modifications have been made in the new generation CPU for AI Agent applications?**

Each generation of HBM undergoes upgrades; the current generation uses HBM4, while the next-generation Rubin platform will clearly adopt Samsung's HBM4E.

On the CPU side, the previous Blackwell platform was equipped with the Grace CPU, while the new Rubin platform will be upgraded to the Vera CPU. The Vera CPU is based on the ARM architecture and can achieve chip-to-chip interconnect with GPUs via NVLink, thereby providing substantial bandwidth. Compared to its previous role as a deeply integrated companion to GPUs, the new generation CPU has seen a significant increase in versatility and can now be sold as a standalone product. For example, NVIDIA has signed an agreement with Meta to directly sell racks based on the Vera CPU in the future, marking that this CPU product line can now compete with x86 CPUs and opening up new products and markets for NVIDIA. Specific software-level optimizations for AI Agent are not yet clear, but both core count and processing power have been enhanced.

**What is the interconnect solution for expanding NVL72 to NVL576?**

The internal interconnect of the NVL72 rack has been confirmed to use an orthogonal backplane solution. When expanding from a single NVL72 rack (72 GPUs) to an NVL576 system composed of 8 racks (576 GPUs), this falls under the scale-up category, and the interconnect solution does not involve direct use of pluggable optical modules between racks. Such cross-rack interconnect is achieved through dedicated CPO racks, specifically using Spectrum-6CPO switches. This solution extends the NVLink domain from a single rack to 8 racks. Since cross-rack distances are typically 10 to 30 meters, optical fiber connections are required, but this is not a traditional optical module solution. This is an optional configuration; customers can choose to build a single 72-card NVLink domain or expand to 576 cards using this solution.

**What is NVIDIA's future roadmap for optical interconnect technology, especially regarding the deployment timeline and solutions for intra-rack optical interconnect?**

NVIDIA's vision is to achieve full optical interconnect, both for scale-up and scale-out scenarios. Currently, in scale-out scenarios, major CSP customers still prefer pluggable optical modules due to ease of maintenance. In high-bandwidth, space-constrained scale-up scenarios, CPO solutions can deliver more significant power savings.

Intra-rack optical interconnect deployment will appear in the Feynman generation of products, which will adopt NVLink 8. The Feynman chip will be tightly coupled with silicon photonics technology, potentially enabling direct optical signal output from the chip.

**What new incremental demand and technical requirements has the LPU rack brought to the PCB industry?**

LPU racks impose extremely high technical requirements on PCBs and represent a significant new growth area in the industry. The PCB for LPU racks will, for the first time, use M9-grade materials, and the number of layers will exceed 70, higher than conventional GPU cards, to meet the extremely high transmission rates and complex routing needs of its chips. The value of the PCB under a single LPU chip is expected to reach $400, and with 256 cards per rack, each rack adds nearly $100,000 in PCB value. Assuming Groq rack shipments reach 20,000 units in 2027, this could bring about $2 billion in incremental demand to the PCB market.

**How do LPU racks and GPU racks work together, and what are their deployment ratios and interconnect methods?**

LPU racks focus on inference and offer extremely fast processing speeds, while NVL72 GPU racks handle long-context computation. In actual deployments, the two need to work in tandem. Since a single LPU card has only 500MB of storage and a single rack offers just over 100GB, this may not be sufficient to hold all parameters of a large model. Therefore, customers purchasing LPU rack solutions will need to configure at least two racks. There is no precise data on the deployment ratio between LPU and GPU racks, but if GPU rack shipments reach 80,000 and LPU racks 20,000 in 2027, this suggests a 4:1 ratio—one LPU rack for every four GPU racks.

Data exchange between the two is achieved via optical interconnect, with the mainstream solution currently being 1.6T pluggable optical modules due to their high standardization and ease of maintenance. Each side adds 256 1.6T optical modules. The solution also reserves the option for CPO, though this may be an optional configuration.

**Google's memory pooling solution uses OCS for connectivity, while NVIDIA seems to achieve this via its DPU chip and NVLink. How do these two technical approaches differ?**

Google uses its proprietary ICI interconnect protocol adapted to OCS. NVIDIA's chip interconnect is mainly based on its proprietary NVLink protocol. NVIDIA's BlueField product has been upgraded to the fourth generation and is essentially a DPU integrating an ARM CPU and a standard ConnectX-7 (CX9) NIC for data processing such as protocol conversion and memory management. The CPU handles intelligent scheduling, while the NIC handles protocol translation. Without the CPU, it is a standard NIC. BlueField mainly handles electrical signals, but in the future, NVIDIA may combine optical communication technology in its memory pooling solution.

**What is the specific architecture of NVIDIA's BlueField solution, and what role does the DPU play?**

This solution uses dedicated memory storage racks. The DPU's role is similar to the component in Google's solution, mainly handling protocol translation and memory resource management. Specifically, NVIDIA's STX architecture uses BlueField-4 for connectivity, which is a storage solution optimized for this DPU. This architecture is an optional configuration rather than standard, and vendors like Oracle are already experimenting with it.

**In NVIDIA's STX architecture, what is the connection method between compute nodes and memory racks, and is there a need for optical modules?**

Compute nodes and memory racks are mainly connected via two protocols: NVIDIA's NVLink or standard Ethernet. General-purpose optical modules (such as 1.6T) can be used to connect storage racks and compute racks. BlueField DPU can be equipped with optical modules to support long-distance data transmission, but this is not standard and can be selected as needed.

**Comparing NVIDIA's BlueField-based solution and Google's OCS-based memory pooling solution, which is more efficient?**

Google's solution may be superior in terms of efficiency and storage utilization. NVIDIA's system essentially still relies on electrical signal processing, with its main advantage being improved storage read/write speeds via BlueField DPU. However, it does relatively little in terms of storage pooling (i.e., allowing a storage server to be dynamically shared by multiple compute racks as needed), and the connection method is relatively fixed. In contrast, the OCS solution leverages optical technology, which inherently offers faster processing speeds and can dynamically switch paths, allocating storage resources to more compute servers as needed, thus achieving higher system efficiency and resource utilization.

**Which supply chain segments or vendors may benefit from NVIDIA's STX storage architecture?**

Storage interface chips will benefit, with Astera Labs products currently more widely used in overseas markets. For short-distance connections, such as communication between adjacent racks, copper cable vendors like Credo also have opportunities. If the rack distance exceeds 7 to 10 meters, optical communication solutions must be used.

**Has Google clarified its memory pooling solution roadmap? What is the current progress?**

Google has internally designated its comprehensive solution based on CXL, memory sharing protocols, and OCS dynamic scheduling as a high-priority project, with plans to launch in 2027. The industry is already developing large-port OCS products with 512 ports to meet Google's requirements for its storage pooling solution. Unlike NVIDIA, which tends to announce externally before systems are fully ready, Google typically only releases solutions after the technology is mature and directly deployed, so the lack of public updates does not mean the project is not progressing.

**What is the relationship between Google's NPO solution and OCS solution?**

NPO (Near-Package Optics) is responsible for transmission, while OCS (Optical Circuit Switch) handles switching. Data output from the chip requires an interface, which can be an optical module, AEC, or NPO. When using the NPO solution, the optical engine is placed close to the chip, and its pigtails (e.g., 64 or more) are directly connected to the OCS switch. OCS directly receives optical fibers from each GPU chip's NPO port and forms a network through switching. In the future, the special high-priced optical modules currently used in OCS solutions will be replaced by the NPO solution.

**When is Google's NPO solution expected to be deployed, and what is its role in the overall compute architecture?**

The NPO solution is expected to be deployed starting in 2027, but not all chips will adopt it. At that time, only high-end training versions of the TPUv9 chip will be equipped with NPO optical interfaces to achieve ultra-large-scale all-to-all peer bandwidth interconnect. Other chip versions will continue to use lower-cost hybrid optical-copper interconnects. The NPO solution is mainly applied at the scale-up level, i.e., inter-chip interconnect.

**How should we understand the trend of OCS application moving from the Spine layer closer to compute nodes?**

Google initially used OCS at the Spine (core switching) layer in general-purpose compute data centers, as this layer has relatively stable traffic and low switching frequency, making it suitable for OCS's slow switching but fast transmission characteristics. Now, OCS applications have expanded to AI compute scale-up networks, directly interconnecting GPU chips. For example, in a system with 9,216 GPUs, optical fibers from each GPU are directly connected to OCS for switching. In the future, the NPO solution will further reinforce this trend: all chip bandwidth will no longer be partially direct-connected but will be fully aggregated to the OCS switch, enabling all-to-all full bandwidth connections between any two chips via the switch. This can be seen as a closer integration of OCS with compute nodes.

**Who is currently the main supplier for Google's NPO solution?**

Currently, Eoptolink Technology Inc. is almost the exclusive supplier for Google's NPO solution. Although other vendors are also communicating with Google, given Eoptolink's leading position in silicon photonics, even if other suppliers enter in the future, Eoptolink is expected to maintain about 70% of the main supply share.

**Lumentum has provided a $1 billion revenue guide for its OCS switch business in 2027. What are the corresponding product specifications, pricing, and shipment expectations behind this?**

Lumentum's revenue guidance corresponds to its 300-port (or 312-port) OCS switches. The product was initially priced at $150,000, with the price expected to drop to around $130,000 as production scales up. Google has indicated that as long as Lumentum can keep up with capacity, future orders could reach 8,000 to 10,000 units. At $130,000 per unit and 8,000 units shipped, this would achieve approximately $1 billion in revenue.

**What is Lumentum's current production capacity, can it meet market demand, and what specific measures are being taken to expand capacity?**

Lumentum's factory in Thailand is undergoing large-scale capacity expansion, with progress going smoothly, but current capacity is still clearly insufficient. To address capacity bottlenecks, Lumentum is considering Chinese contract manufacturers.

**Are all FAUs in current CPO solutions pluggable?**

Yes, all CPO FAUs currently under development are required to be pluggable. Unlike traditional soldered FAUs, this solution requires high-precision, compact wafer-level collimating lenses.

**Welcome to connect! For WeChat ID, please visit Shirley's ACE Basecamp personal homepage~**

Follow-up

[Is Innolight's expected 70% share in Google's NPO already priced in, and how will it materially impact its gross margin?](/chat?title=Is%20Innolight's%20expected%2070%25%20share%20in%20Google's%20NPO%20already%20priced%20in,%20and%20how%20will%20it%20materially%20impact%20its%20gross%20margin?) [With Nvidia's STX architecture introducing memory pooling, can Astera Labs leverage this growth to sustain its current high valuation premium?](/chat?title=With%20Nvidia's%20STX%20architecture%20introducing%20memory%20pooling,%20can%20Astera%20Labs%20leverage%20this%20growth%20to%20sustain%20its%20current%20high%20valuation%20premium?)

cpoocs

2

Dislikes

2

Share

Expert Bio：

头部光模块企业专家

Expert 1-on-1

[![](https://image.acecamptech.com/avatar/50506349/0.461045180007979.png?x-oss-process=style/avatar)](/organizer/20511154)

[Shirley](/organizer/20511154)

Acecamp analyst

Follow

多年二级市场投资研究经验，聚焦AI，研究内容涵盖AI硬件、AI软件、AI应用（机器人、自动驾驶、游戏）等。欢迎交流！微信号：Shirley2025H

Solemn statement: The above content is based on public information, only represents personal or guests' views. It does not represent any position of AceCamp, any companies, any institutions. The volatility of the stock market is related to many factors. Investment decisions are made by individuals based on their own research and analysis. The purpose of this article or event is the sharing of facts and views and does not constitute any investment suggestions. This article or event content must not be forwarded, reproduced, duplicated, published, modified, or quoted in whole or in part by any institution or individual in any form without the permission of AceCamp and the author. The above content is exclusive to paying clients, and all institutions and individuals are strictly bound by confidentiality obligations and intellectual property agreements. AceCamp is not responsible for the impact of any third party's unauthorized acts while maintaining the rights for legal actions.

Related Recommendations

[![](https://image.acecamptech.com/generates/20260313/4e49234f3391.png)

Expert Interview on Optical Interconnects: Key Takeaways from GTC/OFC, Discussing CPO, OCS, Feynman Architecture, and Memory Pooling

2026/03/18 Wed 12:00 Event](/eventDetail/60532843)[Exponential Ramp-Up of 1.6T: ELS and Silicon Photonics Localization as Core Variables

The 1.6T ramp-up is exhibiting exponential growth; domestic capacity expansion cycles have been compressed to 6–8 months, and leading enterprises have largely resolved key material bottlenecks through proactive ordering.
New supply chain risk: Sumitomo’s production cuts due to rare earth supply disruptions have led to severe shortages of rotators, with delivery pressure expected in 2026 Q2, requiring resource locking and domestic substitution.
Competitive landscape: Source Photonics is expected to regain share on the Meta side after resolving grayscale validation issues.

2026/03/16 06:51Note](/article/detail/70559833)[![](https://image.acecamptech.com/generates/20260313/d8dd24d7c1a3.png)

Domestic CCL Leader Expert Exchange - M9/M10 Material Progress, Upstream Material Price Hikes and New Technology Requirements, Domestic Breakthroughs and Competitive Landscape Changes

2026/03/16 Mon 12:00 Event](/eventDetail/60532845)[Who Is Pricing the CPO Sector? —— A Capital Structure Analysis of Seven Key Constituents

1. Analysis of the CPO sector's capital structure and micro-liquidity;
2. Behavioral patterns and competitive dynamics of Northbound, public/quant, and hot money;
3. Quantitative framework for determining pricing power and capital structure profiles for seven core targets.

2026/03/10 01:59Insight](/article/detail/70559613)

[Optical Module Channel Check: Domestic and Overseas Demand in 2026/2027, Silicon Photonics Solutions Expected to Reach 60% Share, Upstream Supply Chain Core Bottleneck Lies in Substrate Materials, Epitaxial Wafer and Substrate Supplier Landscape

- Forecast of domestic and overseas optical module market demand for 2026/2027;
- Ramp-up pace of domestic 1.6T optical modules;
- Upstream supply chain core component capacity (CW laser) and supply bottlenecks.

2026/03/05 02:42Note](/article/detail/70559474)[![](https://image.acecamptech.com/generates/20260315/c319e9bd4494.png)

CPO Expert Talk: Yield Status and Key Bottlenecks in Optical Engines and Co-packaging, Opportunities for Domestic Optical Module Companies, and GTC/OFC Updates

2026/03/19 Thur 14:00 Event](/eventDetail/60532866)[![](https://image.acecamptech.com/generates/20260227/2f3a882473f6.png)

Optical Module Manufacturers Channel Check: Customer Demand and Capacity Layout, LPO/CPO Progress and Future Application Trends, Market Competition Landscape

2026/03/03 Tues 06:00 Event](/eventDetail/60532300)[OFC Points to the Direction of Optical Interconnect Architectures / Distinct Roles for Optical and Copper at Different Stages / LITE, COHR, CIEN, GLW: The Four Titans Enter Another Boom Cycle

1. Lumentum presents a convincing evolution path for optical-copper architectures.
2. Lumentum: Multiple growth engines, sustained prosperity amid supply-demand gap.
3. Coherent: Full-stack capabilities build a moat.
4. Ciena and GLW: Each excels in its own domain.

2026/03/20 08:30Insight](/article/detail/70560020)

[March Update on Leading Gas Turbine Blade Manufacturer—Business Progress and Capacity Expansion

The following insights are provided by industry experts:
1. Recently, the company has engaged with multiple clients in overseas markets, with some already entering the supplier qualification process. Currently, there are over a dozen overseas clients, mainly focused on the gas turbine aftermarket.
2. An agreement was previously signed with Saudi Arabia, and plant planning is underway, but no significant substantive progress has been made yet.
3. Growth in the gas turbine business has exceeded expectations. The future strategic focus is to enter more OEM supply chains to secure longer-term, sustained orders.

2026/03/20 08:21Note](/article/detail/70560016)[Expert Exchange on Domestic CCL Leaders: Progress of M9 and M10 Materials, Upstream Price Increases and New Technical Requirements, Domestic Breakthroughs

M10 material is in the R&D stage, with a comparison of manufacturers submitting samples and their progress.
Changes in technical requirements for upstream raw materials (resin, copper foil, spherical silica micropowder, etc.) for M10 materials.
COWOP R&D progress and core requirements.

2026/03/17 02:58Note](/article/detail/70559868)[Optical Communication Industry Channel Check: OEM Capacity Planning and Product Allocation Expectations, CW Light Source Price and Volume Trends and Supply Chain Competition Landscape, Optical Module Key Component Breakdown—Focus on Hui Lyu/Linktel/Source Photonics/InnoLight/Eoptolink/USI/Yuanjie, etc.

1. OEM capacity planning and product allocation expectations;
2. CW light source price and volume trends and supply chain competition landscape;
3. Optical module key component breakdown.

2026/03/19 09:40Note](/article/detail/70559975)[AI Server Drill Bit Market: Competitive Landscape, Technological Gap, and Cost Considerations

The technological gap is mainly reflected in process, equipment, design, and raw material R&D capabilities.
IC substrate holes are smaller, requiring higher standards for processing technology and materials. Union has a strong competitive advantage in the IC substrate field.
Product iteration is continuously optimized from three dimensions: design, materials, and coating, with process and stability improved through repeated testing and incremental iteration.

2026/03/19 09:36Note](/article/detail/70559973)

[Passive Optical Component Expert Exchange – MPO Price Increase Expectations, AOC Product Ramp-up, CPO Progress, MT Ferrules

Expectations for 800G and 1.6T optical module FAU products in 2026, price changes, and profitability.
Impact of fiber and MT ferrule price increases on MPO manufacturers' profitability and the pass-through situation.
Whether there is a supply shortage in the MT ferrule industry and the progress of domestic manufacturers in validation breakthroughs.

2026/03/19 03:06Note](/article/detail/70559951)[AI-Driven Low CTE Glass Fabric Demand Doubles; Equipment Bottlenecks Constrain Capacity Release and Technology Iteration

AI applications are driving a doubling in Low CTE glass fabric demand, with monthly industry consumption rapidly rising from 1.5–2 million meters and a 30%–40% supply-demand gap for high-end substrate materials.
The main bottleneck for capacity expansion lies in Toyota high-speed looms, whose capacity has been booked through 2030, resulting in Low CTE fabric lead times extending beyond six months and a de facto "order rejection" scenario.
T-fabric prices have risen from RMB 100 to RMB 150; if the RMB 200 ceiling is reached, Q-fabric (pure quartz fabric) will achieve structural substitution due to its cost-effectiveness and low CTE performance.
NVIDIA is advancing Cowop packaging technology, planning to eliminate the substrate and directly connect to the PCB by the end of 2026, which may reduce substrate usage and ease supply pressure on base materials.

2026/03/18 07:21Note](/article/detail/70559928)[Update on Leading Industrial Equipment O&M Provider—Market Share, Sales Channels, and New Products

The following insights are provided by industry experts:
1. The core target customers for the products are large-scale, continuous-process manufacturing enterprises, characterized by equipment that cannot be shut down or where downtime would significantly impact production efficiency. The greater the impact of downtime, the more urgent the demand. Applicable industries include chips, pharmaceuticals, fertilizers, steel, petroleum, and power generation, all of which involve continuous production scenarios.
2. The true core of customer selection lies in two aspects: first, the systematic O&M capability supported by local offices and service personnel; second, the expert service capability and service accuracy.
3. The intelligent diagnostics workflow is: "system automatically monitors and detects issues—intelligent software alarms and pushes notifications—system completes most of the analysis—experts intervene when necessary." In most scenarios, after receiving an alert, on-site maintenance personnel can handle the issue directly if the system has completed the diagnosis or if personnel can make their own judgment.

2026/03/18 07:33Note](/article/detail/70559932)[Recent Developments in PCB Copper Foil—Supply-Demand Dynamics, Capacity Expansion, and Processing Fees

The following insights are provided by industry experts:
1. In terms of PCB copper foil supply and demand for 2024 and 2025, overall capacity can meet market needs. In 2024, domestic PCB copper foil capacity is about 700,000 tons, with actual shipments around 480,000 tons; in 2025, capacity is expected to remain above 700,000 tons, with shipments of approximately 510,000–520,000 tons.
2. In terms of pricing, general-purpose PCB copper foil is currently around RMB 17,000–18,000/ton; RTF series is about RMB 20,000–23,000/ton; HVLP series shows a wide range.
3. Historically, high-end copper foil has long been dominated and priced by Japanese and Taiwanese manufacturers, with domestic supply mainly relying on imports; domestically, RTF began to penetrate the market in 2017 and 2018, while HVLP series started to penetrate from 2024, gradually capturing a small market share.

2026/03/18 06:55Note](/article/detail/70559924)

- 1
- 2
- 3
- 4

Comments

Published

![No Data](https://static.acecamptech.com/system/empty.svg)

No Data

Publisher

[![](https://image.acecamptech.com/avatar/50506349/0.461045180007979.png?x-oss-process=style/avatar)](/organizer/20511154)

[Shirley](/organizer/20511154)

Published 95 Articles

Follow

Latest update

[More>](/organizer/20511154)

- [Interview with Experts from Leading Taiwanese Packaging Companies: Opportunities for Mainland Subsidiaries in the AI Era, Future Positioning, Technical Reserves, and Key Developments

  2026/03/20 02:23](/article/detail/70559988)
- [CPO Expert Exchange – Yield and Key Bottlenecks in Optical Engine and Co-Packaging, Future Timeline, GTC Conference Updates

  2026/03/20 02:21](/article/detail/70559987)
- [Expert Exchange with Leading Domestic Probe Manufacturer – Progress in Cooperation with Overseas Clients such as NV, Changes in GB300 and Rubin Probe Demand, Breakthroughs by Domestic Manufacturers

  2026/03/19 03:51](/article/detail/70559954)

![img](https://static.acecamptech.com/system/posters/en_article_poster.png)

Related Radars

[Hot Radars >](/radars)

- [总结最近1个月各个专家对2026年-2027年光模块的出货量，出货结构，asp的判断

  已关注雷达](/radars?monitor_id=6568fe69-2812-5766-bb27-d78df2282aae)
- [总结最近1个月专家对存储行业的观点，争议和共识，投资机会和风险

  已关注雷达](/radars?monitor_id=c59d4783-4c4e-5c92-b477-95b44c579834)
- 国产 GPU 各公司出货量追踪

  +My Radars
- 光模块的出货量

  +My Radars
- 光模块CPO和NPO新技术趋势

  +My Radars
- 下一季各CSP的CapEX预测

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
