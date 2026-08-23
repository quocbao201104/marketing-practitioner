# Shopee Commerce / Product-Discovery Evidence Ledger

Source identifiers for `../../platforms/commerce/shopee.md`.

This ledger prioritizes Shopee Vietnam buyer/seller documentation because market-specific behavior is material, plus Shopee engineering research for retrieval systems. Reviewed 2026-08-23.

## [S01] Shopee Vietnam — product search, sort/filter, and image search

Shopee Help Center Vietnam. **[Thành viên mới] Cách Tìm Kiếm Sản Phẩm Cần Mua Trên Shopee.** Reviewed 2026-08-23.

Use: current evidence that shoppers can search by keyword or image, and can explicitly sort/filter results by category, seller location, shipping, price, newest, best-selling, ascending/descending price, Freeship, preferred-shop status, ratings, and other criteria.

Boundary: a shopper-selectable filter or sort option does not establish that the same property is a default organic-ranking weight.

## [S02] Shopee Vietnam — buyer-relative displayed price

Shopee Help Center Vietnam. **[Thành viên mới] Về cách thức hiển thị giá trên Sàn TMĐT Shopee.** Reviewed 2026-08-23.

Use: current evidence that Search Results, PDP/Product Information, Today Suggestions, and You May Also Like can display estimated prices after vouchers available in each buyer's account; multi-variant/multi-product postings can show the lowest price among classifications/products. Final checkout price can differ because vouchers are exhausted, sellers change prices, or promotions have time/quantity limits.

Boundary: displayed estimated price is a representation scoped to buyer/time/state, not guaranteed final payable price.

## [S03] Shopee Vietnam — product variations

Shopee Help Center Vietnam. **Thanh Toán Tối Đa 20 Phân Loại Sản Phẩm Cho Mỗi Lần Mua Là Gì?** Reviewed 2026-08-23.

Use: current buyer-facing evidence that product classifications/variations represent choices such as color, size or model on one product page.

Boundary: buyer UI semantics do not establish every seller/backend model ID or API object.

## [S04] Shopee Vietnam — listing policy and information requirements

Shopee Help Center Vietnam. **QUY ĐỊNH VỀ ĐĂNG BÁN SẢN PHẨM TRÊN SHOPEE.** Current policy page reviewed 2026-08-23.

Use: seller listing rules for truthful/clear Vietnamese product names, image/title consistency, detailed descriptions, origin, attributes, warranty where required, correct category selection, category-specific information, and prohibited misleading keywords/content. Shopee states correct category selection helps products reach customers.

Boundary: listing/policy requirements and seller guidance do not reveal organic ranking weights.

## [S05] Shopee Vietnam — seller / shop classifications

Shopee Help Center Vietnam. **Shop Yêu Thích/Shop Yêu Thích+ là gì?; Shopee Mall là gì?** Reviewed 2026-08-23.

Use: current evidence that shop-level classifications/badges exist, can depend on operational/customer-service criteria, appear on shop/product representations, and can be explicitly filtered by shoppers in Search. Shopee Mall is a separately recognized seller/shop regime.

Boundary: visible/filterable shop status does not by itself prove default organic ranking priority.

## [S06] Shopee Vietnam — buyer evaluation / purchase context

Shopee Help Center Vietnam. **[Thành viên mới] Làm sao để mua hàng / đặt hàng trên ứng dụng Shopee?** Reviewed 2026-08-23.

Use: buyer-facing evidence that product choice can include image/name, seller classification, seller location and other product/commercial information; checkout requires account/address/payment/shipping and availability conditions.

Boundary: buyer-visible evaluation cues are not automatically ranking factors.

## [S07] Jiang et al. — MRSE multimodal retrieval at Shopee

Jiang, H., Zhang, H., Hou, Q., Chen, C., Lin, W., Zhang, J., & Wang, A. (2024). **MRSE: An Efficient Multi-modality Retrieval System for Large Scale E-commerce.** arXiv:2408.14968.

Use: Shopee implementation-backed evidence that text-query product retrieval can combine query text, product textual data/images, and user multimodal preferences/history. Online A/B testing reported gains for the disclosed system.

Boundary: does not establish every current 2026 Shopee Search stage, model, ranker, field weight or market.

## [S08] Liu et al. — MIEM for Shopee Image Search

Liu, C., Hou, P., Zeng, A., & Yu, H. (2024). **Transformer-empowered Multi-modal Item Embedding for Enhanced Image Search in E-Commerce.** AAAI 2024 / arXiv:2311.17954.

Use: deployed Shopee Image Search system builds item embeddings from textual information plus multiple product images and reported online click/order improvements after deployment.

Boundary: image-search retrieval system evidence does not establish default text-search ranking rules or direct seller image-ranking tactics.

## [S09] Shopee Vietnam — Sản phẩm Hot visibility feature

Shopee Help Center Vietnam. **ĐIỀU KHOẢN SỬ DỤNG TÍNH NĂNG SẢN PHẨM HOT.** Reviewed 2026-08-23.

Use: evidence that Shopee can operate a distinct product-visibility feature that provides highlighted placements on Search/Recommendations under feature-specific comparative criteria.

Boundary: this is a scoped special visibility/product feature. Do not translate its disclosed criteria into ordinary organic Search/Recommendation ranking factors.

## Evidence-use rules

```text
KEYWORD SEARCH
≠ ONLY DISCOVERY MODE

TEXT QUERY
≠ TEXT-ONLY RETRIEVAL

IMAGE QUERY
≠ IMAGE-ONLY ITEM REPRESENTATION

DEFAULT RANKING
≠ USER SORT
≠ USER FILTER

SHOP BADGE / CLASSIFICATION VISIBLE OR FILTERABLE
≠ PROVEN DEFAULT ORGANIC RANKING WEIGHT

BASE / VARIANT PRICE
≠ BUYER-RELATIVE DISPLAYED PRICE
≠ GUARANTEED CHECKOUT PRICE

PRODUCT VARIATION
≠ NEW DURABLE PRIMITIVE

LISTING RULE / FIELD REQUIREMENT
≠ ORGANIC RANKING FACTOR

SẢN PHẨM HOT FEATURE CRITERIA
≠ ORDINARY ORGANIC SEARCH LAW

ENGINEERING RETRIEVAL MODEL
≠ TIMELESS COMPLETE 2026 PRODUCTION SYSTEM
```
