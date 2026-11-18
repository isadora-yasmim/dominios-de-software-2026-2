# Revisão Final e Consolidação dos Artefatos

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (INF0296, 2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #55 · **Versão:** 1.1 · **Data:** 18/11/2026
**Responsável:** Verônica Ribeiro Oliveira Palmeira (Analista de Qualidade e Documentação; consolidadora, conforme a seção 4.2 do [processo de requisitos](Processo_Requisitos.md))
**Base:** enunciado do Projeto da Disciplina (1ª etapa) e todos os artefatos da `main` em 17/11/2026

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Checklist dos entregáveis da 1ª etapa](#2-checklist-dos-entregáveis-da-1ª-etapa)
3. [Atividades de levantamento pedidas no enunciado](#3-atividades-de-levantamento-pedidas-no-enunciado)
4. [Cobertura do escopo do enunciado](#4-cobertura-do-escopo-do-enunciado)
5. [Revisão cruzada entre integrantes](#5-revisão-cruzada-entre-integrantes)
6. [Consistência dos identificadores e dos artefatos](#6-consistência-dos-identificadores-e-dos-artefatos)
7. [Correções feitas nesta revisão](#7-correções-feitas-nesta-revisão)
8. [Pontos fora do repositório](#8-pontos-fora-do-repositório)
9. [Versionamento](#9-versionamento)
10. [Revisão de conformidade com o enunciado (18/11/2026)](#10-revisão-de-conformidade-com-o-enunciado-18112026)

---

## 1. Objetivo

Conferir, antes da entrega, se a 1ª etapa atende a tudo o que o enunciado pede, se os artefatos estão coerentes entre si e se tudo está versionado. A issue #55 pede quatro verificações, tratadas nas seções abaixo:

| Item da issue #55 | Seção |
|---|---|
| Conferir checklist de entregáveis da 1ª etapa | 2, 3 e 4 |
| Revisão cruzada entre integrantes | 5 |
| IDs de requisitos consistentes em todos os documentos | 6 e 7 |
| Tudo versionado no repositório | 9 |

O que estava inconsistente foi corrigido no próprio artefato, pela gestão de mudanças do processo (seção 9 do processo): a correção entra por PR, com histórico de revisões no artefato alterado. A seção 7 lista essas correções.

---

## 2. Checklist dos entregáveis da 1ª etapa

Itens da lista "Entrega dos seguintes documentos" do enunciado, na mesma ordem.

| # | Entregável pedido | Artefato | Issue | Situação |
|---|---|---|---|---|
| 1 | Planejamento das atividades – estilo Kanban | [Quadro Kanban no GitHub Projects](https://github.com/users/isadora-yasmim/projects/3), com as issues #30 a #56 e o marco "1ª Entrega – Levantamento de Requisitos" | #30 | Atendido |
| 2 | Definição do processo de requisitos | [Processo_Requisitos.md](Processo_Requisitos.md): etapas, técnicas, papéis, RACI, identificação, MoSCoW, rastreabilidade e gestão de mudanças | #31 | Atendido |
| 3 | Síntese dos Requisitos das Entrevistas | [Sintese_Requisitos_Entrevistas.md](elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md): 37 candidatos `RE` | #41 | Atendido |
| 4 | Entrega da entrevista transcrita | [Entrevista01_Adriana.md](elicitacao/entrevistas/Entrevista01_Adriana.md) e [Entrevista02_Eliene.md](elicitacao/entrevistas/Entrevista02_Eliene.md), com roteiros e termo de consentimento | #34, #35, #36 | Atendido |
| 5 | Entrega do questionário preenchido | [Questionario01_Isabella.md](elicitacao/questionarios/Questionario01_Isabella.md) e [Questionario02_Vaneide.md](elicitacao/questionarios/Questionario02_Vaneide.md) | #37, #38, #39 | Atendido |
| 6 | Síntese dos Requisitos dos Questionários | [Sintese.md](elicitacao/questionarios/Sintese.md): 21 candidatos `RQ` | #42 | Atendido |
| 7 | Síntese dos Requisitos do Sistema análogo | [Sintese_Requisitos_Sistema_Analogo.md](elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md): 26 candidatos `RA` | #43 | Atendido |
| 8 | Lista de requisitos – Geral | [Lista_Geral_Requisitos.md](Lista_Geral_Requisitos.md) e [CSV](Lista_Geral_Requisitos.csv): 160 candidatos consolidados em 117 requisitos (65 RF, 36 RNF, 16 RN) | #45 | Atendido |
| 9 | Documento Visão – cap. 7 do Larman | [Documento_Visao.md](Documento_Visao.md) | #46 | Atendido |
| 10 | Diagrama de casos de uso – cap. 6 do Larman | [Diagrama_Casos_de_Uso.md](modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md), fonte [PlantUML](modelagem/casos-de-uso/Diagrama_Casos_de_Uso.puml) e 8 imagens: 7 atores e 31 casos de uso | #47 | Atendido |
| 11 | Casos de uso essenciais, pelo menos 1 completo por integrante – cap. 6 do Larman | [Casos_de_Uso_Completos.md](modelagem/casos-de-uso/Casos_de_Uso_Completos.md): 5 casos completos para 5 integrantes (UC-08, UC-13, UC-14, UC-19, UC-25). Os 31 casos estão em formato resumido no diagrama, seção 4 | #48 | Atendido |
| 12 | Matriz de Rastreabilidade (horizontal e vertical) – requisitos, fontes e artefatos | [Matriz_Rastreabilidade.md](Matriz_Rastreabilidade.md) e [CSV](Matriz_Rastreabilidade.csv): vertical (fonte → requisito → caso de uso → tela → entidade) e horizontal (requisito ↔ requisito) | #49 | Atendido |
| 13 | Protótipos das telas – Figma | [Prototipo.md](prototipacao/Prototipo.md) e [arquivo no Figma](https://www.figma.com/design/yiyjqLFpIp838MAi9x0EW4/Dom%C3%ADnios-de-Software-2026-2?node-id=6-3): 51 telas, 47 web e 4 para celular | #50 | Atendido. Ver a seção 8 |
| 14 | Especificação suplementar para os RNF (ISO/IEC 25010) – cap. 7 do Larman | [Especificacao_Suplementar.md](Especificacao_Suplementar.md): 36 RNF com critério de aceitação e método de verificação, pela ISO/IEC 25010:2023 | #51 | Atendido |
| 15 | Modelo Entidade-Relacionamento / Modelo de domínio | [Modelo_Dominio_ER.md](modelagem/modelo-dados/Modelo_Dominio_ER.md): diagramas Mermaid por área, tratamento do anonimato e rastreabilidade entidade × requisito | #52 | Atendido |
| 16 | Dicionário de dados (glossário): termo, definição, formato (tipo, tamanho, unidade), relacionamento e regra de validação – cap. 7 do Larman | [Dicionario_de_Dados.md](Dicionario_de_Dados.md): glossário de termos de negócio e dicionário de todos os atributos do ER, com tipo, tamanho ou domínio, unidade, obrigatoriedade, chave, relacionamento, regra de validação e classificação LGPD | #53 | Atendido |
| 17 | Especificação de Requisitos – IEEE 830 e/ou EOR | [Especificacao_Requisitos_IEEE830.md](Especificacao_Requisitos_IEEE830.md), no padrão IEEE Std 830-1998 | #54 | Atendido |
| 18 | Todos os artefatos em ferramenta de controle de versões | Este repositório no GitHub | — | Atendido. Ver a seção 9 |

---

## 3. Atividades de levantamento pedidas no enunciado

| Atividade do enunciado | Como foi feita | Evidência |
|---|---|---|
| Busca de documentos: leis, regulamentações, padrões (ISO/IEC 25010) | 21 documentos analisados (`FD-01` a `FD-21`), entre eles LGPD, ISO/IEC 25010:2023, CLT, normas de acessibilidade e guias da ANPD. 59 candidatos `RD` | [Pesquisa_Documental.md](elicitacao/pesquisa-documental/Pesquisa_Documental.md), [Requisitos_Pesquisa_Documental.md](elicitacao/pesquisa-documental/Requisitos_Pesquisa_Documental.md) |
| 2 entrevistas, transcritas e anexadas, com identificação, função e telefone | E01: Adriana Silveira de Souza, Product Owner e professora da disciplina, 20/10/2026, 1h57min de gravação. E02: Eliene de Souza Oliveira, Secretária Municipal de Educação, 17/11/2026, 18 min de gravação. As duas com nome, função e telefone | Seção "Identificação" de cada transcrição |
| 2 questionários com pessoas diferentes das entrevistadas, anexados com as respostas, identificação, função e telefone | Q01 e Q02. As duas com telefone e consentimento LGPD registrado | Seção 1 de cada questionário |
| Pesquisar sistemas análogos e descrever as funcionalidades | 15Five, da lista de sugestões do enunciado, registrado na issue #32. 27 funcionalidades descritas (`FA-01` a `FA-27`), com capturas de tela | [Sistema_Analogo_15Five.md](elicitacao/sistema-analogo/Sistema_Analogo_15Five.md) |
| Processo de negócio de avaliação, com as principais dores, em BPMN | Dois diagramas AS-IS, um por entrevista, com as dores D1 a D6 marcadas, em arquivo `.bpmn` e imagem | [Processo_AS-IS_e_Dores.md](elicitacao/bpmn/Processo_AS-IS_e_Dores.md) e arquivos em [`elicitacao/bpmn/`](elicitacao/bpmn/) |
| Outras técnicas de elicitação | Prototipação no Figma (técnica `RT` do processo, seção 3) | [Prototipo.md](prototipacao/Prototipo.md) |

---

## 4. Cobertura do escopo do enunciado

Cada item do escopo e cada restrição do enunciado tem requisitos e artefatos. A ligação completa está na seção 7 da lista geral e no Apêndice A da especificação IEEE 830.

| Item do enunciado | Requisitos principais | Casos de uso | Telas |
|---|---|---|---|
| Diversos tipos de feedback: chefe-colaborador, pares, 360° | RF-013, RF-024, RF-025, RN-004 | UC-08, UC-13, UC-14 | T-08, T-09, T-32 |
| Feedback formal, informal, positivo e construtivo | RF-013, RF-014, RF-016, RF-022 | UC-08, UC-13 | T-08, T-09 |
| Questionários para apoiar emissores e orientar receptores | RF-007, RF-008, RF-009, RF-027 | UC-05, UC-14 | T-14 a T-18, T-37 |
| Várias fontes de feedback, baseadas em dados coletados dos emissores | RF-011, RF-024, RF-032, RN-001, RN-002 | UC-06, UC-08, UC-16 | T-19, T-42 |
| Análise robusta: tendências, números e recursos visuais | RF-049, RF-050, RNF-007, RNF-020 | UC-22, UC-23 | T-05, T-07, T-39, T-40 |
| Confidencialidade e anonimato | RF-019, RF-030, RN-004, RN-005, RNF-001 a RNF-003 | UC-13, UC-14 | T-15, T-16, T-32 |
| Acompanhamento por plano de ação; histórico dos feedbacks | RF-042 a RF-045, RF-048, RN-003, RN-006 | UC-19, UC-20, UC-22 | T-20 a T-22, T-25 a T-27 |
| Planejamento de desenvolvimento: metas ao longo do tempo | RF-046, RF-047, RF-049 | UC-21, UC-22 | T-23, T-24 |
| Plataforma web, com perspectiva de dispositivos móveis | RNF-027, RNF-028, RNF-030, RNF-035, RNF-036 | Todos | T-48 a T-51 |
| Consonância com a LGPD | RF-053 a RF-063, RNF-031, RN-011 a RN-013, RN-016 | UC-25 a UC-30 | T-04, T-41 |

---

## 5. Revisão cruzada entre integrantes

Todo artefato entrou na `main` por pull request. A seção 4.2 do processo exige revisão por um integrante diferente do autor. Pelo histórico do Git, em 21 dos 22 PRs o merge foi feito por um integrante diferente do autor do primeiro commit do PR. A exceção é o #74, que reúne casos de uso de vários integrantes, tem commits de Júlia, Davi e Verônica e foi integrado pela Verônica, também autora de parte dele. Em outros quatro PRs (#59, #63, #71 e #76), quem integrou também tem um commit de correção no próprio PR. A coluna Autor e quem integrou vêm do histórico do Git. A informação "Aprovado" vem do GitHub e não pode ser conferida pelo histórico do Git. Dados de 17/11/2026.

| PR | Artefato | Autor | Revisão e integração |
|---|---|---|---|
| #28 | Transcrição da Entrevista 1 | Isadora | Integrado por Júlia |
| #29 | Questionário 01 | Isadora | Integrado por Júlia |
| #57 | Questionário 02 | Isadora | Aprovado e integrado por Júlia |
| #58 | Roteiro de entrevista e termo de consentimento | Júlia | Integrado por Isadora |
| #59 | Pesquisa documental | Isadora | Aprovado e integrado por Júlia |
| #60 | Descrição do sistema análogo 15Five | Júlia | Aprovado e integrado por Davi |
| #61 | Processo de requisitos | Júlia | Aprovado e integrado por Davi |
| #62 | Síntese do sistema análogo | Júlia | Aprovado e integrado por Davi |
| #63 | Síntese dos questionários | Isadora | Aprovado e integrado por Júlia |
| #64 | Transcrição da Entrevista 2 | Ana Luísa | Aprovado e integrado por Isadora |
| #65 | Síntese das entrevistas | Davi | Aprovado e integrado por Isadora |
| #66 | Lista geral de requisitos | Verônica | Aprovado e integrado por Isadora |
| #67 | BPMN AS-IS e dores | Ana Luísa | Aprovado e integrado por Isadora |
| #68 | Modelo de domínio e ER | Isadora | Aprovado e integrado por Júlia |
| #69 | Documento Visão | Ana Luísa | Aprovado e integrado por Júlia |
| #70 | Diagrama de casos de uso | Davi | Aprovado por Isadora, integrado por Verônica |
| #71 | Especificação suplementar | Verônica | Aprovado e integrado por Júlia |
| #72 | Protótipo no Figma | Júlia | Aprovado e integrado por Verônica |
| #73 | Dicionário de dados e glossário | Ana Luísa | Aprovado e integrado por Verônica |
| #74 | Casos de uso completos (UC-08, UC-13, UC-14, UC-19, UC-25) | Júlia, Davi e Verônica (pelos commits) | Aprovado e integrado por Verônica |
| #75 | Especificação IEEE 830 | Verônica | Aprovado e integrado por Júlia |
| #76 | Matriz de rastreabilidade | Davi | Aprovado e integrado por Ana Luísa |

Além da revisão de cada PR, os artefatos de especificação revisaram os anteriores e registraram as divergências encontradas: o dicionário de dados (seção 5), a especificação IEEE 830 (Apêndice C) e a matriz de rastreabilidade (seção 8). Esta revisão final aplicou as correções que esses registros pediam (seção 7).

---

## 6. Consistência dos identificadores e dos artefatos

As conferências abaixo foram feitas por script sobre todos os arquivos `.md` e `.csv` do repositório, depois das correções da seção 7.

| # | Conferência | Resultado |
|---|---|---|
| 1 | A lista geral tem 117 requisitos: 65 RF, 36 RNF e 16 RN; 61 Must, 44 Should, 8 Could e 4 Won't | Conforme |
| 2 | Todo identificador `RF-`, `RNF-` e `RN-` citado em qualquer documento existe na lista geral | Conforme |
| 3 | Texto e observações dos requisitos iguais na lista geral (.md) e no CSV | Conforme, 117 de 117 |
| 4 | Texto, prioridade e origem iguais na lista geral e na matriz (CSV) | Conforme, 117 de 117 |
| 5 | Texto e prioridade iguais na lista geral e na especificação IEEE 830 | Conforme, 117 de 117 |
| 6 | Texto dos RNF igual na lista geral e na especificação suplementar | Conforme, 36 de 36 |
| 7 | Ligação RF → caso de uso igual no diagrama de casos de uso e na matriz | Conforme, 65 de 65 |
| 8 | 31 casos de uso com o mesmo nome no diagrama, na matriz e nos títulos dos casos completos | Conforme |
| 9 | Entidades de cada requisito iguais na matriz e na seção 12 do modelo ER | Conforme |
| 10 | Mesmas entidades no modelo ER e no dicionário de dados | Conforme, 56 entidades |
| 11 | Mesmos atributos no modelo ER e no dicionário de dados | Conforme |
| 12 | Mesmos valores de enumeração no modelo ER e no dicionário de dados | Conforme |
| 13 | Links internos e âncoras entre os documentos | Conforme, nenhum link quebrado |
| 14 | Mesmo nome do produto nos cabeçalhos dos artefatos ("Sistema Web de Feedback e Gestão de Competências", decisão ERS-D01) | Conforme |

**Identificadores usados no projeto.** Requisitos definitivos `RF-xxx`, `RNF-xxx`, `RN-xxx`; candidatos por técnica `RE`, `RQ`, `RD`, `RA`, `RP`; casos de uso `UC-xx`; telas `T-xx`; dores `D1` a `D6`; decisões `C-xx` e `P-xx` (lista geral), `DS-xx` (especificação suplementar), `M-xx` (modelo ER), `UCxx-Dnn` (casos completos), `ERS-Dxx` (especificação IEEE 830); pontos do dicionário `G-xx`, `I-xx`, `T-xx`. Todos seguem a seção 5 do processo de requisitos.

---

## 7. Correções feitas nesta revisão

Têm histórico de revisões, com a linha da versão 1.1, sete artefatos: a lista geral, o modelo ER, o dicionário de dados, a especificação IEEE 830, a especificação suplementar, o Documento Visão e a matriz de rastreabilidade. Os casos de uso UC-08 e UC-19, que tiveram conteúdo alterado, também receberam histórico de revisões. Os demais arquivos alterados não têm histórico próprio; as alterações deles estão registradas no histórico do Git.

| Artefato | Correção | Motivo |
|---|---|---|
| [Lista geral](Lista_Geral_Requisitos.md) (1.1) e CSV | RF-003 passa a incluir os perfis diretoria e encarregado; RN-005 registra que o mínimo de respondentes nunca é menor que 3; RN-006 trata o plano de ação de feedback confidencial | Alterações indicadas pela especificação IEEE 830 (Apêndice C.3; decisões ERS-D02, ERS-D08, ERS-D05) e ainda não aplicadas |
| Lista geral | A seção 9 passa a "Pontos decididos pelo grupo, sem confirmação da PO". As observações chamam cada decisão de "decisão do grupo, não confirmada pela PO" | Os dez pontos ainda não foram confirmados pela PO. As decisões são do grupo e continuam sujeitas à confirmação dela |
| [Modelo ER](modelagem/modelo-dados/Modelo_Dominio_ER.md) (1.1) | Perfis `DIRETORIA` e `ENCARREGADO`; autor das versões e rascunho de feedback confidencial; `Feedback.peso`; regra do prazo de retenção; remoção de `Meta.atingida`; enumerações fechadas; `CheckInMeta`, `CheckInPlano`, `DestinatarioVisibilidade`, `DisponibilidadeAgenda`, `TermoOfensivo`; controle de falhas de login; `Fato.observado_equipe_id`; novos valores de notificação e de status do plano; `PlanoAcao.gestor_id` | Inconsistências I-01 e I-04 a I-13 do dicionário, decisões UC08-D01, UC08-D02 e UC19-D01 dos casos completos e Apêndice C.2 da especificação IEEE 830, que pediam esses ajustes |
| [Dicionário de dados](Dicionario_de_Dados.md) (1.1) | Entidades e atributos conforme o ER 1.1; glossário de perfis, 360° e equipe; inventário LGPD e prazos; coluna "Tratamento" em todos os pontos da seção 5 | Manter o dicionário igual ao ER e registrar como cada ponto foi resolvido |
| [Especificação IEEE 830](Especificacao_Requisitos_IEEE830.md) (1.1) | Textos de RF-003, RN-005 e RN-006; entidades novas na seção 3.4.1; situação dos apêndices C.2 e C.3 | Refletir a lista geral 1.1 e o ER 1.1 |
| [Especificação suplementar](Especificacao_Suplementar.md) (1.1) | Linha do encarregado na matriz de acesso (seção 8.1); situação das decisões DS-01 e DS-09; DS-10 como decisão do grupo, ainda não confirmada pela PO | Igualar à especificação IEEE 830 (seção 3.6.5) e atualizar as decisões marcadas "a validar" |
| [Documento Visão](Documento_Visao.md) (1.1) | Seção 8 registra os pontos P-xx como decisões do grupo, ainda não confirmadas pela PO; perfis ligados ao RF-003; link para o glossário | Coerência com a lista geral 1.1 e com o dicionário, que já existe |
| [Matriz de rastreabilidade](Matriz_Rastreabilidade.md) (1.1) e CSV | Textos novos; ligações horizontais do RF-003; entidades do ER 1.1; situação das pendências; tabela 4.2 sem a coluna de página, que divergia da seção 4.1 | Refletir as correções acima |
| [UC-19 Criar plano de ação](modelagem/casos-de-uso/UC-19_Criar_Plano_de_Acao.md) (1.1) | Extensão 1e e decisão UC19-D04 para feedback confidencial | O caso de uso permitia ao par confidencial definir o plano com o receptor, o que revelaria o emissor (RN-004, RN-006) |
| UC-08 e UC-19 | Indicação de que o impacto no ER foi aplicado | Decisões UC08-D01, UC08-D02 e UC19-D01 |
| [Diagrama de casos de uso](modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) | Decisão sobre a diretoria como perfil sem ator próprio; seção 9 atualizada; link para os casos completos | Coerência com o RF-003 e com os artefatos já entregues |
| Sínteses das entrevistas, dos questionários e do sistema análogo, e pesquisa documental | Os pontos que estavam "a validar" mostram onde foram decididos na lista geral | Mostrar o destino de cada ponto aberto na fase de elicitação |
| [Protótipo](prototipacao/Prototipo.md) | Resumo das 51 telas por fluxo, com ligação à matriz | O documento só tinha o link do Figma |
| Cabeçalhos de todos os artefatos | Nome do produto padronizado | Decisão ERS-D01 e ponto T-08 do dicionário |
| [README](../README.md) | Tabela de integrantes com nome e papel; índice com os caminhos certos, os números reais das issues e o item do enunciado de cada artefato | Os links de quatro artefatos apontavam para a pasta `docs/`, e os números de issue misturavam a numeração dos cartões com a do GitHub |

---

## 8. Pontos fora do repositório

Estes pontos dependem de ferramentas fora do Git e não alteram nenhum requisito.

| # | Ponto | Situação |
|---|---|---|
| 1 | Anotações de 9 telas no Figma citam requisitos diferentes dos da lista geral | Corrigidas na matriz (seção 4.2), que é a referência. A atualização das anotações é feita no arquivo do Figma |
| 2 | Casos de uso sem tela no protótipo, entre eles UC-03, UC-04 e UC-28, que atendem requisitos Must | Registrados na matriz (seções 4.1 e 8). Os requisitos continuam rastreados pelo caso de uso e pela entidade |
| 3 | Imagens exportadas do modelo ER (pasta `img/`) | Mostram a versão 1.0. Os diagramas Mermaid da página do modelo, renderizados pelo GitHub, são a fonte e já estão na versão 1.1 |
| 4 | Imagens PNG e SVG do diagrama de casos de uso | Resolvido em 18/11/2026: todas as imagens foram geradas de novo a partir do `.puml`, e o UC-19 aparece ligado ao Colaborador |
| 5 | PDFs exportados do Figma, usados para numerar as telas `T-xx` na matriz | Não estão no repositório. A coluna "Pág. do PDF" da matriz (seção 4.1) não pode ser conferida por quem não tem os PDFs |

---

## 9. Versionamento

Todos os artefatos estão no repositório [isadora-yasmim/dominios-de-software-2026-2](https://github.com/isadora-yasmim/dominios-de-software-2026-2), em Markdown, CSV, BPMN, PlantUML, PNG e SVG. Cada artefato entrou por uma branch própria e um pull request ligado à sua issue (seção 5), e o histórico de cada arquivo está no Git. O único artefato mantido fora do Git é o arquivo de telas do Figma, que o enunciado pede nessa ferramenta. O repositório guarda o link e a descrição das telas ([Prototipo.md](prototipacao/Prototipo.md)).

---

## 10. Revisão de conformidade com o enunciado (18/11/2026)

Depois do merge do PR #77, todo o repositório foi lido de novo e comparado, item a item, com o enunciado do Projeto da Disciplina: transcrições, questionários, pesquisa documental, sistema análogo, BPMN, sínteses, lista geral, Documento Visão, casos de uso, especificações, modelo ER, dicionário, matriz e protótipo. Os critérios foram os do próprio enunciado, os modelos de Larman (caps. 6 e 7) e a lista de verificação da seção 2.4 do processo de requisitos. Nenhum identificador, prioridade ou total da lista geral mudou.

| Artefato | Correção | Motivo |
|---|---|---|
| [Entrevista 01](elicitacao/entrevistas/Entrevista01_Adriana.md) | Telefone da entrevistada preenchido | O enunciado pede identificação com nome, função e telefone. O campo estava "N/A" |
| [Documento Visão](Documento_Visao.md) (1.2) | Nova seção 2.4, Alternativas e concorrência; coluna Prioridade na tabela de necessidades | Seções do modelo de Documento Visão de Larman (cap. 7) que faltavam: alternativas usadas hoje e concorrentes, e prioridade de cada necessidade |
| [UC-19](modelagem/casos-de-uso/UC-19_Criar_Plano_de_Acao.md) (1.2) | Ator principal: Colaborador, no papel de emissor, chamado de Gestor no cenário | O caso completo dizia "Gestor", e o diagrama e o `.puml` ligam o UC-19 ao Colaborador |
| [Síntese dos questionários](elicitacao/questionarios/Sintese.md) | Prioridades em MoSCoW (11 Must, 10 Should, 1 Could), no lugar de Alta, Média e Baixa | O processo (seção 7) e as outras sínteses usam MoSCoW. A correspondência mantém as mudanças de prioridade explicadas na lista geral, como "subiu de Could para Should" no RF-040 |
| Síntese e Questionário 02 | Citação da resposta aberta igual à transcrição literal ("alguns situação") | A citação entre aspas tinha sido corrigida, o que a tornava diferente da resposta registrada |
| [Processo AS-IS e dores](elicitacao/bpmn/Processo_AS-IS_e_Dores.md) | Retirada a observação sobre o número da issue no README, que já estava resolvida; justificativa para não modelar o TO-BE | A observação estava desatualizada |
| [Dicionário de dados](Dicionario_de_Dados.md), ponto T-08 | Texto da divergência original do nome do sistema | A padronização do nome tinha deixado as duas metades da linha iguais, e a divergência deixava de fazer sentido |
| [Protótipo](prototipacao/Prototipo.md) (1.2) | Cabeçalho com responsáveis, versão e base; papel do protótipo no processo e limitações conhecidas | Padrão dos demais artefatos e transparência sobre as pendências da matriz |
| Documento Visão, lista geral, matriz e esta revisão | Os pontos P-01 a P-10 são descritos só como decisões do grupo ainda não confirmadas pela PO | Registrar a situação dos pontos sem atribuir motivo à PO |
| README, pesquisa documental, BPMN e roteiros | "360°" com o símbolo de grau | Grafia definida no glossário (termo Avaliação 360°). Os nomes dos elementos dos diagramas BPMN foram mantidos como estão nas imagens |
| [Sistema análogo](elicitacao/sistema-analogo/Sistema_Analogo_15Five.md) | Link para a síntese do sistema análogo no cabeçalho | O artefato relacionado era citado sem link |
| [Especificação IEEE 830](Especificacao_Requisitos_IEEE830.md) (1.2) | Definição de Avaliação 360° igual à do glossário; definição de Plano de ação com o caso confidencial; ator do UC-19; texto da ERS-D01; matriz no Apêndice E | A definição de 360° ("todos avaliam todos") contradizia a decisão ERS-D09 e o RF-025, e a seção 1.3.1 declara transcrever o glossário sem alteração |
| [Dicionário de dados](Dicionario_de_Dados.md) (1.2) | Termos Plano de ação, Emissor e Receptor com a regra do feedback confidencial; `Feedback.data_feedback` não futura; `AcaoPlano.responsavel_id` e `meta_acao`; `RegistroAuditoria.ator_id` e `ip_origem` opcionais nas rotinas automáticas; contato do encarregado no agente de pequeno porte | Coerência com a RN-006 1.1, com as decisões UC08-D05 e UC19-D02, com o UC-19 (toda ação tem meta) e com o UC-30, cuja eliminação automática não tem usuário mas precisa ser auditada |
| [Modelo ER](modelagem/modelo-dados/Modelo_Dominio_ER.md) (1.2) | Cardinalidade zero ou um entre `Colaborador` e `RegistroAuditoria` | Mesma razão do item anterior |
| [Especificação suplementar](Especificacao_Suplementar.md) (1.2) | Links para os artefatos relacionados; seção 12.3 com os itens do modelo de Larman sem requisito nesta etapa | Seções do modelo de Larman (cap. 7) que não estavam registradas |

**Conferências refeitas depois das correções:** links internos e âncoras de todos os arquivos `.md` (nenhum quebrado); citações literais conferidas com as transcrições; texto dos 117 requisitos igual na lista geral, no CSV e na especificação IEEE 830, e dos 36 RNF na especificação suplementar; definições da IEEE 830 iguais às do glossário.

