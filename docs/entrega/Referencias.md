# Referências

**Projeto:** Sistema Web de Feedback e Gestão de Competências · **Etapa:** 2ª Entrega – Arquitetura e Desenho Detalhado
**Versão:** 1.0 · **Issue:** #107 · **Autora:** Isadora Yasmim da Silva · **Revisora:** Ana Luísa Pereira dos Santos

| Item | Descrição |
|---|---|
| Tipo e natureza | Lista consolidada de referências (documento de apoio, não é modelo do sistema) |
| Propósito | Reunir, sem repetição, todas as fontes citadas nos artefatos do projeto, conforme a regra 5 da seção 7 do enunciado |
| Público-alvo | Integrantes do grupo, docente/PO e leitores do documento final |
| Uso no documento final | Entra no PDF depois da última seção e antes dos apêndices (issue #109) |

---

## Sumário

1. [Regras desta lista](#1-regras-desta-lista)
2. [Livros](#2-livros)
3. [Normas técnicas e especificações](#3-normas-técnicas-e-especificações)
4. [Legislação e regulamentos](#4-legislação-e-regulamentos)
5. [Artigos e guias técnicos](#5-artigos-e-guias-técnicos)
6. [Sistema análogo (15Five)](#6-sistema-análogo-15five)
7. [Dados de mercado](#7-dados-de-mercado)
8. [Uso de inteligência artificial](#8-uso-de-inteligência-artificial)
9. [Referências sugeridas ainda não usadas](#9-referências-sugeridas-ainda-não-usadas)
10. [Histórico de revisões](#10-histórico-de-revisões)

---

## 1. Regras desta lista

1. **Só entra o que foi citado.** Cada referência está em pelo menos um artefato do repositório, no item onde foi usada (coluna **Usada em**). Nenhum dado foi completado de memória: autor, ano, edição e URL são os que aparecem nos documentos de origem.
2. **Identificador único.** Cada referência tem um identificador `REF-nn`, que nunca é reaproveitado. Referências novas recebem o próximo número livre da sua seção.
3. **Citação no item.** O artefato que usa uma fonte a cita no próprio texto e na sua seção de referências. Esta lista não substitui essas citações; ela as consolida para o PDF.
4. **Uso de IA.** Cada uso registra organização e ferramenta, URL, data de acesso e o que foi feito. Como os prompts têm mais de um parágrafo, eles ficam no [Apêndice II](apendices/Apendice_II_Prompts_IA.md) e a referência indica "Questão: Apêndice II, Seção II.n" (seção 8 do enunciado).
5. **Atualização automática.** O script [`scripts/verificar_referencias.py`](../../scripts/verificar_referencias.py) compara as seções de referências de todos os documentos em `docs/` com esta lista e aponta o que falta. Qualquer integrante pode rodá-lo com `python3 scripts/verificar_referencias.py`. Quem usa o Claude Code pode ligá-lo a hooks, que pedem ao assistente que complete esta lista e o Apêndice II sempre que uma referência nova aparecer.
6. **Fontes internas.** Entrevistas, questionários, pesquisa documental e demais artefatos do projeto são citados nos próprios documentos, com link, e não se repetem aqui.

---

## 2. Livros

| ID | Referência | Usada em |
|---|---|---|
| REF-01 | LARMAN, C. *Utilizando UML e Padrões: uma introdução à análise e ao projeto orientados a objetos e ao desenvolvimento iterativo*. 3. ed. Porto Alegre: Bookman, 2007. Caps. 6 (casos de uso), 7 (outros requisitos: Documento Visão, especificação suplementar, modelo FURPS+ e glossário) e 13 (arquitetura lógica em camadas). <!-- alias: LARMAN Utilizando UML Padrões --> | Cap. 6: [Diagrama de casos de uso](../modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md), [Casos de uso completos](../modelagem/casos-de-uso/Casos_de_Uso_Completos.md) e UC-08, UC-13, UC-14, UC-19, UC-25. Cap. 7: [Documento Visão](../especificacao/Documento_Visao.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Dicionário de dados](../especificacao/Dicionario_de_Dados.md). Caps. 6 e 7: [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [README](../../README.md). Cap. 13: Decisões arquiteturais (#80, PR #115) |

---

## 3. Normas técnicas e especificações

| ID | Referência | Usada em |
|---|---|---|
| REF-10 | IEEE. *IEEE Std 830-1998 – Recommended Practice for Software Requirements Specifications*. 1998. <!-- alias: IEEE 830 Práticas recomendadas especificação requisitos software --> | [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [Processo de requisitos](../planejamento/Processo_Requisitos.md), [Revisão final](Revisao_Final.md), [README](../../README.md) |
| REF-11 | ISO/IEC/IEEE 29148:2018 – *Systems and software engineering – Life cycle processes – Requirements engineering*. | [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), seção 1.4 |
| REF-12 | ISO/IEC. [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) – *Systems and software engineering – Systems and software Quality Requirements and Evaluation (SQuaRE) – Product quality model*. <!-- alias: ISO/IEC 25010 Modelo qualidade produto software --> | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [Lista geral](../analise/Lista_Geral_Requisitos.md), [README](../../README.md) |
| REF-13 | ARC42. [ISO 25010 update 2023](https://quality.arc42.org/articles/iso-25010-update-2023). Resumo das mudanças da edição de 2023. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), seção 9 |
| REF-14 | ABNT. [ABNT NBR 17225:2025](https://www2.camara.leg.br/a-camara/estruturaadm/gestao-na-camara-dos-deputados/responsabilidade-social-e-ambiental/acessibilidade/pdfs/ABNTNBR17225AcessibilidadeDigitalparaWeb.pdf) – Acessibilidade em conteúdo e aplicações web – Requisitos. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [Documento Visão](../especificacao/Documento_Visao.md), [Lista geral](../analise/Lista_Geral_Requisitos.md), casos de uso completos |
| REF-15 | ABNT. ABNT NBR 17060:2022 – Acessibilidade em aplicativos de dispositivos móveis – Requisitos. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Lista geral](../analise/Lista_Geral_Requisitos.md) |
| REF-16 | W3C. [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). 2023. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [Documento Visão](../especificacao/Documento_Visao.md), [Protótipo](../prototipacao/Prototipo.md), [Lista geral](../analise/Lista_Geral_Requisitos.md), casos de uso completos |
| REF-17 | BRASIL. [eMAG – Modelo de Acessibilidade em Governo Eletrônico](https://emag.governoeletronico.gov.br/). | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), seção 9 |
| REF-18 | NIST. [SP 800-63B-4 – Digital Identity Guidelines: Authentication and Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html). 2025. Seção 2 (níveis AAL, reautenticação) e seção 3.2.2 (limitação de tentativas). | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md) (DS-05, DS-06), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), Decisões arquiteturais (#80, PR #115) |
| REF-19 | IETF. [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180) – Common Format and MIME Type for Comma-Separated Values (CSV) Files. 2005. | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md) |
| REF-20 | IETF. [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) – The JavaScript Object Notation (JSON) Data Interchange Format. 2017. | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md) |
| REF-21 | IETF. [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238) – TOTP: Time-Based One-Time Password Algorithm. 2011. | Decisões arquiteturais (#80, PR #115), ADR-08 |
| REF-22 | IETF. [RFC 6265](https://www.rfc-editor.org/rfc/rfc6265) – HTTP State Management Mechanism (cookies). 2011. | Decisões arquiteturais (#80, PR #115) |
| REF-23 | IETF. [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457) – Problem Details for HTTP APIs. 2023. | Decisões arquiteturais (#80, PR #115) |
| REF-24 | OpenAPI Initiative. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html). | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), Decisões arquiteturais (#80, PR #115) |

---

## 4. Legislação e regulamentos

| ID | Referência | Usada em |
|---|---|---|
| REF-30 | BRASIL. [Lei nº 13.709, de 14 de agosto de 2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) – Lei Geral de Proteção de Dados Pessoais (LGPD). <!-- alias: Lei 13.709/2018 LGPD resoluções ANPD --> | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md), [Documento Visão](../especificacao/Documento_Visao.md), [Dicionário de dados](../especificacao/Dicionario_de_Dados.md), [Lista geral](../analise/Lista_Geral_Requisitos.md), [README](../../README.md), Decisões arquiteturais (#80, PR #115; arts. 33, 46 e 48) |
| REF-31 | BRASIL. [Lei nº 12.965, de 23 de abril de 2014](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm) – Marco Civil da Internet. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), Decisões arquiteturais (#80, PR #115; art. 15) |
| REF-32 | BRASIL. [Lei nº 13.146, de 6 de julho de 2015](http://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13146.htm) – Lei Brasileira de Inclusão da Pessoa com Deficiência. <!-- alias: Lei 13.146/2015 Lei Brasileira Inclusão ABNT NBR 17225:2025 WCAG 2.2 --> | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md), [Especificação IEEE 830](../especificacao/Especificacao_Requisitos_IEEE830.md) |
| REF-33 | BRASIL. [Constituição da República Federativa do Brasil de 1988](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm). | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-34 | BRASIL. [Decreto-Lei nº 5.452, de 1º de maio de 1943](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm) – Consolidação das Leis do Trabalho (CLT). | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-35 | BRASIL. [Lei nº 9.029, de 13 de abril de 1995](https://www.planalto.gov.br/ccivil_03/leis/l9029.htm) – Proíbe práticas discriminatórias na relação de trabalho. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Lista geral](../analise/Lista_Geral_Requisitos.md) |
| REF-36 | BRASIL. [Lei nº 14.611, de 3 de julho de 2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14611.htm) – Igualdade salarial e de critérios remuneratórios entre mulheres e homens. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-37 | BRASIL. [Lei nº 14.457, de 21 de setembro de 2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14457.htm) – Programa Emprega + Mulheres. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Lista geral](../analise/Lista_Geral_Requisitos.md) |
| REF-38 | MTE. Portaria MTE nº 1.419, de 27 de agosto de 2024 – nova redação do capítulo 1.5 da NR-1; Portaria MTE nº 765, de 15 de maio de 2025 – prorroga a vigência para maio de 2026. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-39 | ANPD. [Resolução CD/ANPD nº 2, de 27 de janeiro de 2022](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022) – Regulamento de aplicação da LGPD para agentes de tratamento de pequeno porte. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-40 | ANPD. [Resolução CD/ANPD nº 15, de 24 de abril de 2024](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-15-de-24-de-abril-de-2024-556243024) – Regulamento de Comunicação de Incidente de Segurança. <!-- alias: ANPD Resolução CD/ANPD 15/2024 comunicação incidentes 19/2024 transferência internacional dados --> | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md) |
| REF-41 | ANPD. [Resolução CD/ANPD nº 18, de 16 de julho de 2024](https://www.in.gov.br/en/web/dou/-/resolucao-cd/anpd-n-18-de-16-de-julho-de-2024-572632074) – Regulamento sobre a atuação do encarregado. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-42 | ANPD. Resolução CD/ANPD nº 19, de 23 de agosto de 2024 – Regulamento de Transferência Internacional de Dados. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Especificação suplementar](../especificacao/Especificacao_Suplementar.md) |
| REF-43 | ANPD. Guia Orientativo – Hipóteses legais de tratamento de dados pessoais: legítimo interesse. Fev. 2024. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-44 | ANPD. [Minuta do Guia de Anonimização e Pseudonimização para a Proteção de Dados Pessoais – Nota Técnica de abertura da consulta](https://www.gov.br/anpd/pt-br/acesso-a-informacao/participacao-social/outras-acoes/ts-01-2024-nota-tenica-6-de-abertura.pdf/@@display-file/file). 2024. | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |
| REF-45 | ANPD. Resolução CD/ANPD nº 31, de 22 de dezembro de 2025 – altera a Agenda Regulatória 2025-2026 ([resumo](https://legismap.com.br/conteudos/artigos-e-noticias/anpd-publica-mapa-de-temas-prioritarios-para-o-bienio-2026-2027-e-atualiza-agenda-regulatoria-2025-2026)). | [Pesquisa documental](../elicitacao/pesquisa-documental/Pesquisa_Documental.md) |

---

## 5. Artigos e guias técnicos

| ID | Referência | Usada em |
|---|---|---|
| REF-50 | NYGARD, M. [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). 2011. | Decisões arquiteturais (#80, PR #115): formato dos ADR |
| REF-51 | OWASP. [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html). | Decisões arquiteturais (#80, PR #115) |
| REF-52 | OWASP. [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html). | Decisões arquiteturais (#80, PR #115) |
| REF-53 | RICHARDSON, C. [Pattern: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html). | Decisões arquiteturais (#80, PR #115) |

---

## 6. Sistema análogo (15Five)

Todas as páginas foram acessadas em 17 nov. 2026 e são citadas na [descrição do sistema análogo](../elicitacao/sistema-analogo/Sistema_Analogo_15Five.md), seção 11.

| ID | Referência |
|---|---|
| REF-60 | 15FIVE. [Pricing](https://www.15five.com/pricing). Atualizado em fev. 2026. Acesso em: 17 nov. 2026. |
| REF-61 | 15FIVE. [Security](https://www.15five.com/security). Acesso em: 17 nov. 2026. |
| REF-62 | 15FIVE. [Pulse – Feature Overview](https://success.15five.com/hc/en-us/articles/50988838569627). Acesso em: 17 nov. 2026. |
| REF-63 | 15FIVE. [Use a company value hashtag in a high five](https://success.15five.com/hc/en-us/articles/16767917040539). Acesso em: 17 nov. 2026. |
| REF-64 | 15FIVE. [Who can see feedback in 15Five?](https://success.15five.com/hc/en-us/articles/50989064497435). Acesso em: 17 nov. 2026. |
| REF-65 | 15FIVE. [Request feedback from a colleague](https://success.15five.com/hc/en-us/articles/50988819903387). Acesso em: 17 nov. 2026. |
| REF-66 | 15FIVE. [1-on-1 permissions and visibility](https://success.15five.com/hc/en-us/articles/50988120900507). Acesso em: 17 nov. 2026. |
| REF-67 | 15FIVE. [Create a review cycle](https://success.15five.com/hc/en-us/articles/360006582292-Create-a-review-cycle). Acesso em: 17 nov. 2026. |
| REF-68 | 15FIVE. [Configure peer and upward review settings (Admin)](https://success.15five.com/hc/en-us/articles/50988326579227-Configure-peer-and-upward-review-settings-Admin). Acesso em: 17 nov. 2026. |
| REF-69 | 15FIVE. [Competencies and Paths overview](https://success.15five.com/hc/en-us/articles/14449983728283). Acesso em: 17 nov. 2026. |
| REF-70 | 15FIVE. [Create and manage a career goal using growth plans](https://success.15five.com/hc/en-us/articles/29897015755931). Acesso em: 17 nov. 2026. |
| REF-71 | 15FIVE. [How does engagement survey confidentiality work in 15Five?](https://success.15five.com/hc/en-us/articles/50988317173275). Acesso em: 17 nov. 2026. |
| REF-72 | 15FIVE. [Set a confidentiality threshold for engagement campaigns](https://success.15five.com/hc/en-us/articles/50988900102043). Acesso em: 17 nov. 2026. |
| REF-73 | 15FIVE. [Install the 15Five mobile app](https://success.15five.com/hc/en-us/articles/51864481442587-Install-the-15Five-mobile-app). Acesso em: 17 nov. 2026. |
| REF-74 | G2. [15Five Reviews](https://www.g2.com/products/15five/reviews). Acesso em: 17 nov. 2026. |
| REF-75 | CAPTERRA. [15Five Reviews](https://www.capterra.com/p/140437/15Five/reviews/). Acesso em: 17 nov. 2026. |

---

## 7. Dados de mercado

| ID | Referência | Usada em |
|---|---|---|
| REF-80 | STATCOUNTER. [Browser Market Share Brazil](https://gs.statcounter.com/browser-market-share/all/brazil). Consulta em novembro de 2026, dados de setembro de 2026. | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md) |

---

## 8. Uso de inteligência artificial

Os prompts completos, na ordem em que foram enviados, estão no [Apêndice II](apendices/Apendice_II_Prompts_IA.md). Em todos os casos o texto gerado foi revisado pela autora do artefato e passa pela revisão de outro integrante no pull request.

| ID | Referência | Usada em |
|---|---|---|
| REF-90 | ANTHROPIC. Claude Code (modelo Claude Opus 5.5). Disponível em: https://claude.com/claude-code. Acesso em: 17 nov. 2026. Usado para redigir o modelo de domínio e entidade-relacionamento, com os diagramas em Mermaid, a partir da issue #52 e dos artefatos da 1ª etapa. Questão: Apêndice II, Seção II.1. | [Modelo de domínio e ER](../modelagem/modelo-dados/Modelo_Dominio_ER.md), seção 15 |
| REF-91 | ANTHROPIC. Claude Code (modelo Claude Opus 5.5). Disponível em: https://claude.com/claude-code. Acesso em: 19 nov. 2026. Usado para redigir o planejamento da 2ª etapa e a tabela de autoria e revisão a partir da issue #78. Questão: Apêndice II, Seção II.2. | Planejamento da 2ª etapa (#78, PR #114) |
| REF-92 | ANTHROPIC. Claude Code (modelo Claude Opus 5.5). Disponível em: https://claude.com/claude-code. Acesso em: 22 nov. 2026. Usado para redigir a primeira versão das decisões arquiteturais a partir da issue #80 e dos artefatos da 1ª etapa. Questão: Apêndice II, Seção II.3. | Decisões arquiteturais (#80, PR #115), seção 7 |
| REF-93 | ANTHROPIC. Claude Code (modelo Claude Opus 5.5). Disponível em: https://claude.com/claude-code. Acesso em: 22 nov. 2026. Usado para consolidar esta lista a partir das seções de referências dos artefatos, redigir o Apêndice II a partir dos registros das sessões e escrever o verificador de referências. Questão: Apêndice II, Seção II.4. | Esta lista, [Apêndice II](apendices/Apendice_II_Prompts_IA.md) e [`scripts/verificar_referencias.py`](../../scripts/verificar_referencias.py) |

---

## 9. Referências sugeridas ainda não usadas

A issue #107 sugere as fontes abaixo. Elas entram nas seções 2 a 5 quando algum artefato da 2ª etapa as citar, com os dados da edição efetivamente consultada.

| Fonte sugerida | Onde deve ser usada | Situação |
|---|---|---|
| ISO/IEC/IEEE 12207 (processos de ciclo de vida de software) | Introdução (#81) | Ainda não citada |
| LARMAN, cap. 11 (contratos de operação) | Contratos CTR-01 a CTR-03 (#105) | Ainda não citado; quando for, acrescentar o capítulo à REF-01 |
| RFC 9110 (semântica do HTTP: métodos, cabeçalhos e status) | Seção 4 – ambiente operacional web (#84, #85) | Ainda não citada |

---

## 10. Histórico de revisões

| Versão | Data | Autor(a) | Alteração |
|---|---|---|---|
| 1.0 | 22/11/2026 | Isadora Yasmim da Silva | Versão inicial: referências consolidadas dos artefatos da 1ª etapa e das decisões arquiteturais (#80), com os usos de IA registrados no Apêndice II (issue #107) |
