# Síntese dos Requisitos do Sistema Análogo – 15Five

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Técnica de elicitação:** Análise de sistema análogo
**Issue:** #43 · **Data:** 17/11/2026
**Entrada:** [Sistema_Analogo_15Five.md](Sistema_Analogo_15Five.md) (funcionalidades `FA-01` a `FA-27`)
**Artefatos relacionados:** [Requisitos_Sistema_Analogo.csv](Requisitos_Sistema_Analogo.csv) (mesma tabela da seção 3, para a matriz de rastreabilidade)

---

## Sumário

1. [Objetivo e método](#1-objetivo-e-método)
2. [Resumo das decisões](#2-resumo-das-decisões)
3. [Requisitos candidatos](#3-requisitos-candidatos)
4. [Funcionalidades descartadas](#4-funcionalidades-descartadas)
5. [Requisitos que vêm das falhas do 15Five](#5-requisitos-que-vêm-das-falhas-do-15five)
6. [Pontos em aberto e tratamento na lista geral](#6-pontos-em-aberto-e-tratamento-na-lista-geral)

---

## 1. Objetivo e método

**Objetivo.** Transformar as funcionalidades analisadas no 15Five em requisitos candidatos para o nosso sistema, e decidir para cada uma se será adotada, adaptada ou descartada.

**Método.**

1. Cada funcionalidade `FA-xx` foi comparada com o que a PO pediu na [Entrevista 01](../entrevistas/Entrevista01_Adriana.md), com os questionários (`RQ-xx`) e com a pesquisa documental (`RD-xx`).
2. Cada funcionalidade recebeu uma das decisões abaixo.
3. As funcionalidades adotadas ou adaptadas viraram requisitos candidatos `RA-xx`, seguindo o padrão de identificação do [processo de requisitos](../../Processo_Requisitos.md).
4. Os pontos fracos do 15Five também geraram requisitos, porque mostram o que o nosso sistema deve fazer diferente (seção 5).
5. A prioridade segue os critérios MoSCoW do processo de requisitos. Ela é uma proposta e será confirmada na lista geral (#45).

| Decisão | Significado |
|---|---|
| **Adotar** | A funcionalidade entra como está no 15Five |
| **Adaptar** | A ideia entra, mas mudada para atender a PO, a LGPD ou o nosso domínio |
| **Descartar** | A funcionalidade não entra, com justificativa |

---

## 2. Resumo das decisões

| Decisão | Quantidade de funcionalidades |
|---|---|
| Adotar | 9 |
| Adaptar | 14 |
| Descartar | 4 |
| **Total analisado** | **27** |

| Requisitos candidatos gerados | Quantidade |
|---|---|
| A partir de funcionalidades adotadas ou adaptadas | 23 |
| A partir das falhas do 15Five | 3 |
| **Total** | **26** |

| Por tipo | Quantidade |
|---|---|
| RF – funcional | 20 |
| RNF – não funcional | 2 |
| RN – regra de negócio | 4 |

| Por prioridade proposta | Quantidade |
|---|---|
| Must | 12 |
| Should | 10 |
| Could | 4 |

Algumas funcionalidades adaptadas tiveram uma parte descartada. Essas partes aparecem na seção 4.

---

## 3. Requisitos candidatos

| ID | Requisito candidato | Tipo | Origem no 15Five | Decisão | Prioridade | Relação com outras fontes |
|---|---|---|---|---|---|---|
| RA-01 | O sistema deve permitir registrar acompanhamentos periódicos (check-ins) entre gestor e colaborador, com frequência configurável, vinculados às metas e aos planos de ação em andamento. | RF | FA-01 | Adaptar | Should | Entrevista 01 §4 e §5; RQ-01 |
| RA-02 | O gestor deve poder registrar fatos e comportamentos observados de um colaborador, com data, ao longo do período. Esses registros ficam visíveis só para o autor até serem vinculados a um feedback. | RF | FA-04 | Adaptar | Must | Entrevista 01 §1 e §2; RD-44 |
| RA-03 | O sistema deve permitir enviar um feedback positivo informal de forma rápida, a qualquer momento, para qualquer colaborador. | RF | FA-05 | Adaptar | Should | Entrevista 01 §3 e §20 (as pessoas dão pouco feedback positivo) |
| RA-04 | Todo feedback deve poder ser vinculado a uma ou mais competências do cargo do receptor. | RF | FA-06 | Adaptar | Must | Entrevista 01 §9; RQ-02 |
| RA-05 | Antes do envio, o sistema deve mostrar ao emissor quem poderá ver o feedback e a identidade dele, de acordo com o modo de identificação definido para aquele tipo de feedback. | RF | FA-07 | Adaptar | Must | RD-15; RD-16 |
| RA-06 | O colaborador deve poder solicitar feedback a um ou mais colegas a qualquer momento, fora do ciclo formal, informando o tema e o prazo de resposta. | RF | FA-08 | Adotar | Should | RQ-06 |
| RA-07 | A visibilidade de um feedback é definida no envio e não pode ser ampliada depois sem nova ação explícita do emissor. | RN | FA-09 | Adotar | Should | RD-22 |
| RA-08 | O gestor deve poder agendar a sessão de feedback com o colaborador, com pauta compartilhada, itens de ação e notas privadas de cada participante. | RF | FA-10 | Adaptar | Should | Entrevista 01 §11 (o gestor agenda a reunião) |
| RA-09 | O administrador deve poder criar ciclos de avaliação formal, com nome, participantes, modalidades e datas de início e fim de cada etapa. | RF | FA-11 | Adotar | Must | Entrevista 01 §17; RQ-01 |
| RA-10 | Um mesmo ciclo deve poder reunir autoavaliação, avaliação do gestor, avaliação por pares e avaliação ascendente (360°). | RF | FA-12 | Adotar | Must | Entrevista 01 §12 e §21; RQ-15 |
| RA-11 | O colaborador avaliado deve poder indicar pares avaliadores, respeitando os números mínimo e máximo do ciclo, com aprovação do gestor. | RF | FA-13 | Adotar | Should | Entrevista 01 §21 |
| RA-12 | O administrador deve poder definir, por ciclo e por modalidade, se a identidade dos pares e dos liderados será exibida ao avaliado. | RF | FA-14 | Adotar | Must | Entrevista 01 §11; RQ-04; RQ-13; RD-15 |
| RA-13 | Antes da liberação dos resultados, o RH deve poder ocultar uma resposta inadequada. A resposta não é apagada, a ação fica registrada em trilha de auditoria e o emissor é avisado. | RF | FA-15 | Adaptar | Should | Entrevista 01 §20; RD-20; RD-38 |
| RA-14 | O administrador deve poder criar modelos de perguntas reutilizáveis, por competência e por cargo, para usar em vários ciclos. | RF | FA-16 | Adotar | Must | Entrevista 01 §15; RQ-02; RD-40 |
| RA-15 | Ao preencher uma avaliação formal, o avaliador deve ver os feedbacks e os fatos registrados sobre o avaliado no período do ciclo, dentro das regras de visibilidade. | RF | FA-18 | Adotar | Should | Entrevista 01 §15; RQ-09 |
| RA-16 | O sistema deve permitir cadastrar metas de desenvolvimento individuais, com indicador, valor esperado, prazo e progresso. | RF | FA-19 | Adaptar | Should | Entrevista 01 §5; RQ-08 |
| RA-17 | O administrador deve poder cadastrar competências e associá-las aos cargos, separando competências fixas do cargo e competências específicas. | RF | FA-20 | Adotar | Must | Entrevista 01 §9; RQ-02 |
| RA-18 | A partir de um feedback construtivo, o sistema deve permitir criar um plano de ação com ações, responsáveis, pontos de monitoramento e data final, e registrar ao fim se houve melhora. | RF | FA-21 | Adaptar | Must | Entrevista 01 §4; RQ-07; RQ-17 |
| RA-19 | Resultados de avaliações confidenciais ou anônimas só podem ser exibidos de forma agregada quando houver um número mínimo de respondentes, configurável. | RN | FA-22 | Adaptar | Must | RQ-14; RD-17 |
| RA-20 | O sistema deve exibir a evolução do colaborador por competência ao longo dos ciclos, informando o período e o número de respostas de cada indicador. | RF | FA-24 | Adaptar | Should | Entrevista 01 §15; RQ-10; RQ-18; RD-43 |
| RA-21 | Ao escrever um feedback, o emissor deve ver orientações e exemplos da estrutura do feedback positivo e do construtivo. | RF | FA-25 | Adaptar | Could | Entrevista 01 §3; RQ-03; RD-37 |
| RA-22 | Quando existir o aplicativo móvel, ele deve oferecer as mesmas funções em iOS e Android, a partir da mesma API da versão web. | RNF | FA-26 | Adaptar | Could | RQ-20; RD-41 |
| RA-23 | O sistema deve permitir login único (SSO) com o provedor de identidade da organização. | RF | FA-27 | Adaptar | Could | RD-39 |
| RA-24 | Todo feedback deve ter campos obrigatórios: emissor, receptor, data, tipo (positivo ou construtivo), modalidade (formal ou informal) e fatos que o motivaram. | RN | Falha do 15Five | Novo | Must | Entrevista 01 §2; RD-44 |
| RA-25 | A interface, as mensagens e os modelos de perguntas devem estar em português do Brasil. | RNF | Falha do 15Five | Novo | Must | RD-57 |
| RA-26 | As perguntas dos acompanhamentos periódicos devem poder variar entre um período e outro, para evitar respostas repetidas. | RN | Falha do 15Five | Novo | Could | — |

---

## 4. Funcionalidades descartadas

| Funcionalidade | Decisão | Justificativa |
|---|---|---|
| FA-02 Pulse: nota de bem-estar em cada check-in | Descartar | Mede humor e bem-estar, o que se aproxima de dado de saúde. A pesquisa documental proíbe usar dados de feedback para monitorar a saúde do colaborador (RD-49). Também foge do foco em fatos pedido pela PO. |
| FA-03 Prioridades semanais | Descartar | É gestão de tarefas, fora do escopo de feedback e competências. |
| FA-17 Calibração de notas entre gestores | Descartar | Serve para equalizar notas usadas em promoção e remuneração. A PO pediu foco em desenvolvimento, não em promoção ou salário (Entrevista 01 §8), e o sistema não decide sobre carreira (RD-46). |
| FA-23 Painel de clima por grupo | Descartar | Depende do Pulse (FA-02), descartado pelo mesmo motivo. |
| Pesquisa de engajamento (parte de FA-22) | Descartar | Pesquisa de clima não faz parte do escopo. Só a regra de mínimo de respondentes foi aproveitada, em RA-19. |
| Visibilidade "somente o gestor" (parte de FA-07) | Descartar | Esconde o feedback de quem o recebe. A PO disse que o receptor tem acesso aos próprios feedbacks e sabe quem é o emissor (Entrevista 01 §11). |
| Reconhecimento público em mural (parte de FA-05) | Descartar | Expor feedback para toda a empresa contraria a privacidade por padrão (RD-22). O feedback positivo continua existindo em RA-03, com visibilidade restrita. |

---

## 5. Requisitos que vêm das falhas do 15Five

Os pontos fracos levantados na [seção 7 da descrição](Sistema_Analogo_15Five.md#7-pontos-fortes-e-pontos-fracos) mostram o que o nosso sistema deve fazer melhor.

| Falha no 15Five | Como o nosso sistema responde |
|---|---|
| Feedback é texto livre, sem fatos nem tipo | RA-24 torna fatos, tipo e modalidade obrigatórios |
| Plano de desenvolvimento não nasce de um feedback | RA-18 cria o plano de ação a partir do feedback construtivo |
| Sem suporte a português | RA-25 exige interface em português do Brasil |
| Usuários repetem respostas no check-in | RA-26 permite variar as perguntas |
| Personalização limitada | RA-14 e RA-17 tornam competências e perguntas configuráveis; reforça RD-40 |
| Relatórios fracos para consolidar avaliações | RA-20 exige painel de evolução por competência; reforça RQ-16 |
| Apps diferentes entre iOS e Android | RA-22 exige as mesmas funções nas duas plataformas |
| Dados hospedados fora do Brasil | Já coberto por RD-28 na pesquisa documental |

---

## 6. Pontos em aberto e tratamento na lista geral

Os pontos abaixo ficaram em aberto ao fim desta síntese. Todos foram decididos na consolidação da [lista geral](../../Lista_Geral_Requisitos.md) (#45), como indicado em cada item.

1. **Registro de fatos antes do feedback (RA-02).** A PO falou em coletar e registrar fatos e depois ligá-los a um feedback. Confirmar se esse registro prévio deve ser uma função própria ou só um campo do feedback. **Tratamento:** conflito C-05 da lista geral, função própria de registro de fatos (RF-011).
2. **Check-ins periódicos (RA-01).** Confirmar se o acompanhamento entre sessões de feedback deve existir para todos os colaboradores ou só para quem tem plano de ação aberto. **Tratamento:** ponto P-09, o gestor define para quais colaboradores da equipe os check-ins valem (RF-041).
3. **Indicação de pares (RA-11).** Confirmar se quem indica os pares é o avaliado, o gestor ou o RH. **Tratamento:** conflito C-01, o gestor seleciona os participantes do seu time (RF-025).
4. **Moderação pelo RH (RA-13).** Confirmar se o RH pode ocultar respostas inadequadas antes da liberação, já que a PO disse que feedback não pode ser apagado. **Tratamento:** ponto P-07, o RH pode ocultar sem apagar, com auditoria e aviso ao emissor (RF-035).
5. **Feedback positivo rápido (RA-03).** Confirmar se o feedback informal positivo precisa ter fatos obrigatórios como os demais (RA-24) ou se pode ter um formulário simplificado. **Tratamento:** conflito C-04, formulário simplificado com fato obrigatório (RF-015, RN-002).
