# Matriz de Rastreabilidade

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #49 · **Versão:** 1.2 · **Data:** 18/11/2026
**Responsável:** Davi Augusto Ferreira de Carvalho
**Artefatos relacionados:** [Matriz_Rastreabilidade.csv](Matriz_Rastreabilidade.csv) (todas as colunas, uma linha por requisito, para filtrar em planilha)

## Histórico de revisões

| Versão | Data | Descrição | Autor |
|---|---|---|---|
| 1.0 | 17/11/2026 | Versão inicial | Davi Augusto Ferreira de Carvalho |
| 1.1 | 17/11/2026 | Revisão final (#55): textos do RF-003, da RN-005 e da RN-006 conforme a lista geral 1.1, com as novas ligações horizontais do RF-003 (RF-061, RF-063, RNF-001); entidades novas do modelo ER 1.1 na coluna Entidades; situação das pendências na seção 8; tabela 4.2 sem a coluna de página, que divergia da seção 4.1 | Verônica Ribeiro Oliveira Palmeira |
| 1.2 | 18/11/2026 | Telas exportadas do Figma para o repositório (`prototipacao/telas/`), no lugar dos PDFs; telas T-52 a T-54 (UC-03, UC-04 e UC-28); anotações do Figma corrigidas; cobertura da seção 7 e pendências da seção 8 atualizadas | Verônica Ribeiro Oliveira Palmeira |

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Vertical e horizontal](#2-vertical-e-horizontal)
3. [Artefatos ligados](#3-artefatos-ligados)
4. [Telas do protótipo](#4-telas-do-protótipo)
5. [Rastreabilidade vertical](#5-rastreabilidade-vertical)
6. [Rastreabilidade horizontal](#6-rastreabilidade-horizontal)
7. [Verificação de cobertura](#7-verificação-de-cobertura)
8. [Pendências encontradas](#8-pendências-encontradas)
9. [Como manter a matriz](#9-como-manter-a-matriz)

---

## 1. Objetivo

Ligar cada requisito da [lista geral](Lista_Geral_Requisitos.md) (#45) às fontes de onde veio e aos artefatos que o tratam: casos de uso, telas do protótipo, entidades do modelo de dados e especificação suplementar. Com a matriz é possível:

- confirmar que nenhum requisito ficou sem origem ou sem artefato (seção 7);
- fazer a análise de impacto de uma mudança, como pede a gestão de mudanças do [processo de requisitos](../planejamento/Processo_Requisitos.md) (seção 9): a linha do requisito mostra tudo o que precisa ser revisto.

---

## 2. Vertical e horizontal

A issue e o processo de requisitos usam os termos de formas diferentes:

| Termo | Na issue #49 | No processo de requisitos (seção 8) |
|---|---|---|
| Vertical | Requisito ↔ fonte | Segue o requisito entre níveis: fonte → requisito → caso de uso → tela → entidade |
| Horizontal | Requisito ↔ artefatos (casos de uso, telas, entidades, RNF) | Liga requisitos do mesmo nível que dependem uns dos outros ou conflitam |

Esta matriz segue o **processo de requisitos**, que foi aprovado pelo grupo e usa a definição comum na literatura. Ele também cobre tudo o que a issue pede:

| Item da issue | Onde está |
|---|---|
| Requisito ↔ fonte (documento, entrevista, questionário, sistema análogo) | Seção 5, colunas Fontes e Origem |
| Requisito ↔ casos de uso, telas e entidades | Seção 5, colunas Casos de uso, Telas e Entidades |
| Requisito ↔ RNF | Seção 6, coluna "RN e RNF aplicáveis", e seção 5.2 |
| Nenhum requisito sem origem ou sem artefato | Seção 7 |

---

## 3. Artefatos ligados

| Ligação | Artefato | De onde a matriz tira a ligação |
|---|---|---|
| Fonte → requisito | [Lista geral](Lista_Geral_Requisitos.md) (#45) | Coluna Origem de cada requisito. O caminho de cada candidato até a fonte (seção da entrevista, pergunta do questionário, lei, funcionalidade do 15Five, dor do BPMN) está na seção 11 da lista geral e nas sínteses de cada técnica |
| Requisito → caso de uso | [Diagrama de casos de uso](../modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) (#47) e [casos de uso completos](../modelagem/casos-de-uso/Casos_de_Uso_Completos.md) (#48) | Coluna Requisitos da seção 4 do diagrama. Dos cinco casos completos, as linhas de RNF e de regras de negócio da seção 13 (Rastreabilidade) |
| Requisito → tela | [Protótipo no Figma](../prototipacao/Prototipo.md) (#50) | Anotações "requisitos atendidos" de cada tela, conferidas com a lista geral (seção 4) |
| Requisito → entidade | [Modelo de domínio e ER](../modelagem/modelo-dados/Modelo_Dominio_ER.md) (#52) | Seção 12, entidade × requisito |
| RNF → característica e verificação | [Especificação suplementar](../especificacao/Especificacao_Suplementar.md) (#51) | Seção 16.1 (RNF) e seção 14 (regras de negócio) |
| Requisito ↔ requisito | Lista geral | Requisitos citados no texto e nas observações de cada requisito, conflitos resolvidos (C-xx, seção 8) e pontos decididos na consolidação (P-xx, seção 9) |

**Códigos das fontes.** Entrevista (`RE`, ou trecho `E01 §n` usado diretamente), Questionário (`RQ`), Pesquisa documental (`RD`), Sistema análogo (`RA`), BPMN AS-IS (`RP`) e Enunciado do trabalho (`ESC`). Como na lista geral, o BPMN foi feito a partir das entrevistas e não conta como fonte independente.

---

## 4. Telas do protótipo

As telas do [protótipo](../prototipacao/Prototipo.md) (#50) foram exportadas do Figma para a pasta [`prototipacao/telas/`](../prototipacao/telas/), uma imagem por tela, com o nome do identificador (`T-01.jpg` a `T-54.jpg`). A coluna Imagem abre a tela.

- **versão web:** 50 telas, `T-01` a `T-47` e `T-52` a `T-54`;
- **versão para celular:** 4 telas, `T-48` a `T-51`.

As telas `T-52` a `T-54` foram criadas na revisão de 18/11/2026 para os requisitos Must que não tinham tela (RF-005, RF-006 e RF-062). Elas recebem os próximos números livres, conforme a seção 9. As anotações do protótipo foram **conferidas** com a lista geral e, depois, corrigidas no Figma (seção 4.2).

### 4.1 Catálogo das telas

| Tela | Imagem | Nome | Perfil | Casos de uso | Requisitos |
|---|---|---|---|---|---|
| T-01 | [ver](../prototipacao/telas/T-01.jpg) | Entrar (login) | Todos | — | RF-003, RNF-022, RF-053, RF-064, RF-065, RN-009 |
| T-02 | [ver](../prototipacao/telas/T-02.jpg) | Verificação em duas etapas | RH, Administrador | — | RF-003, RNF-006 |
| T-03 | [ver](../prototipacao/telas/T-03.jpg) | Entrar – erro de login | Todos | — | RNF-021 |
| T-04 | [ver](../prototipacao/telas/T-04.jpg) | Primeiro acesso – como tratamos seus dados | Colaborador | UC-25, UC-26 | RF-053, RF-055, RN-012 |
| T-05 | [ver](../prototipacao/telas/T-05.jpg) | Início – painel do colaborador | Colaborador | UC-22 | RF-048, RF-049, RNF-007, RNF-020 |
| T-06 | [ver](../prototipacao/telas/T-06.jpg) | Início – sem feedbacks (estado vazio) | Colaborador | UC-22, UC-09 | RF-049, RF-031 |
| T-07 | [ver](../prototipacao/telas/T-07.jpg) | Evolução por competência – dados em tabela | Colaborador | UC-22 | RF-049, RNF-007, RNF-020 |
| T-08 | [ver](../prototipacao/telas/T-08.jpg) | Dar feedback – informal | Colaborador | UC-08 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RN-001, RN-002, RN-003, RN-004, RNF-012, RNF-013 |
| T-09 | [ver](../prototipacao/telas/T-09.jpg) | Dar feedback – formal (ciclo) | Gestor | UC-08 | RF-013, RF-016, RF-019, RF-022, RF-023, RN-004 |
| T-10 | [ver](../prototipacao/telas/T-10.jpg) | Dar feedback – erro: nenhum fato vinculado | Colaborador | UC-08 | RN-001, RN-002, RNF-021 |
| T-11 | [ver](../prototipacao/telas/T-11.jpg) | Dar feedback – confirmar envio | Colaborador | UC-08 | RF-019, RN-003, RNF-015 |
| T-12 | [ver](../prototipacao/telas/T-12.jpg) | Dar feedback – alerta de termo ofensivo | Colaborador | UC-08 | RNF-024 |
| T-13 | [ver](../prototipacao/telas/T-13.jpg) | Feedback enviado | Colaborador | UC-08, UC-11, UC-19 | RF-037, RF-042 |
| T-14 | [ver](../prototipacao/telas/T-14.jpg) | Avaliações pendentes | Avaliador convidado | UC-14 | RF-027 |
| T-15 | [ver](../prototipacao/telas/T-15.jpg) | Responder avaliação – modo confidencial | Avaliador convidado | UC-14 | RF-019, RF-027, RF-028, RN-004, RN-005, RNF-012, RNF-014 |
| T-16 | [ver](../prototipacao/telas/T-16.jpg) | Responder avaliação – modo anônimo | Avaliador convidado | UC-14 | RF-019, RN-004, RN-005 |
| T-17 | [ver](../prototipacao/telas/T-17.jpg) | Responder avaliação – confirmar envio | Avaliador convidado | UC-14 | RF-019, RNF-015 |
| T-18 | [ver](../prototipacao/telas/T-18.jpg) | Avaliações – após o envio | Avaliador convidado | UC-14 | RF-027 |
| T-19 | [ver](../prototipacao/telas/T-19.jpg) | Resultado do ciclo | Colaborador | UC-16, UC-22 | RF-032, RF-033, RN-005, RN-007, RN-008, RNF-007 |
| T-20 | [ver](../prototipacao/telas/T-20.jpg) | Novo plano de ação | Gestor | UC-19 | RF-042, RN-006 |
| T-21 | [ver](../prototipacao/telas/T-21.jpg) | Acompanhar plano de ação | Colaborador | UC-20 | RF-043 |
| T-22 | [ver](../prototipacao/telas/T-22.jpg) | Plano de ação – data final | Gestor | UC-20 | RF-043, RN-006 |
| T-23 | [ver](../prototipacao/telas/T-23.jpg) | Metas e planos de ação | Colaborador | UC-21 | RF-046, RF-047 |
| T-24 | [ver](../prototipacao/telas/T-24.jpg) | Nova meta | Colaborador | UC-21 | RF-046, RN-006 |
| T-25 | [ver](../prototipacao/telas/T-25.jpg) | Feedbacks recebidos e enviados | Colaborador | UC-22 | RF-048, RF-020, RN-003 |
| T-26 | [ver](../prototipacao/telas/T-26.jpg) | Detalhe do feedback, com versões e réplica | Colaborador | UC-10, UC-22 | RF-020, RN-003, RN-004 |
| T-27 | [ver](../prototipacao/telas/T-27.jpg) | Histórico do colaborador – visão do RH | RH | UC-24 | RF-048, RF-051, RNF-005 |
| T-28 | [ver](../prototipacao/telas/T-28.jpg) | Ciclos de avaliação | RH, Gestor | UC-13, UC-15 | RF-022 |
| T-29 | [ver](../prototipacao/telas/T-29.jpg) | Planejar ciclo 1/6 – dados gerais | RH, Gestor | UC-13 | RF-022 |
| T-30 | [ver](../prototipacao/telas/T-30.jpg) | Planejar ciclo 2/6 – objetivos e indicadores | RH, Gestor | UC-13 | RF-022, RF-023 |
| T-31 | [ver](../prototipacao/telas/T-31.jpg) | Planejar ciclo 3/6 – competências e questionário | RH, Gestor | UC-13 | RF-022 |
| T-32 | [ver](../prototipacao/telas/T-32.jpg) | Planejar ciclo 4/6 – modalidades e privacidade | RH, Gestor | UC-13 | RF-024, RF-030, RN-004, RN-005 |
| T-33 | [ver](../prototipacao/telas/T-33.jpg) | Planejar ciclo 5/6 – participantes e datas | RH, Gestor | UC-13 | RF-022, RF-025 |
| T-34 | [ver](../prototipacao/telas/T-34.jpg) | Planejar ciclo 6/6 – revisão e abertura | RH, Gestor | UC-13 | RF-022, RF-026 |
| T-35 | [ver](../prototipacao/telas/T-35.jpg) | Acompanhar ciclo | RH, Gestor | UC-15 | RF-029, RF-040 |
| T-36 | [ver](../prototipacao/telas/T-36.jpg) | Encerrar ciclo – confirmação | RH, Gestor | UC-15, UC-16 | RN-005, RNF-015 |
| T-37 | [ver](../prototipacao/telas/T-37.jpg) | Competências e questionários | RH | UC-05 | RF-007, RF-008, RF-009, RN-001, RN-014 |
| T-38 | [ver](../prototipacao/telas/T-38.jpg) | Moderação antes de liberar resultados | RH | UC-17 | RF-035, RN-003, RNF-005 |
| T-39 | [ver](../prototipacao/telas/T-39.jpg) | Minha equipe – painel do gestor | Gestor | UC-23 | RF-044, RF-050, RN-005, RNF-007, RNF-020 |
| T-40 | [ver](../prototipacao/telas/T-40.jpg) | Painel da organização | RH | UC-23 | RF-050, RN-005 |
| T-41 | [ver](../prototipacao/telas/T-41.jpg) | Meus dados (direitos do titular) | Colaborador | UC-25, UC-26 | RF-055, RF-056, RF-057, RF-058, RF-059, RF-060 |
| T-42 | [ver](../prototipacao/telas/T-42.jpg) | Registrar fato | Colaborador | UC-06 | RF-011 |
| T-43 | [ver](../prototipacao/telas/T-43.jpg) | Pedir feedback | Colaborador | UC-09 | RF-031 |
| T-44 | [ver](../prototipacao/telas/T-44.jpg) | Usuários e estrutura – importação de planilha | RH, Administrador | UC-01, UC-02 | RF-001, RF-002 |
| T-45 | [ver](../prototipacao/telas/T-45.jpg) | Declaração de acessibilidade | Todos | — | RF-065 |
| T-46 | [ver](../prototipacao/telas/T-46.jpg) | Agendar sessão de feedback | Gestor | UC-11 | RF-037, RF-038, RF-039 |
| T-47 | [ver](../prototipacao/telas/T-47.jpg) | Notificações | Todos | UC-31 | RF-040 |
| T-48 | [ver](../prototipacao/telas/T-48.jpg) | Início – celular (área visível) | Colaborador | UC-22 | RF-048, RF-049, RNF-027 |
| T-49 | [ver](../prototipacao/telas/T-49.jpg) | Início – celular (página inteira) | Colaborador | UC-22 | RF-048, RF-049, RNF-007, RNF-020, RNF-027 |
| T-50 | [ver](../prototipacao/telas/T-50.jpg) | Dar feedback – celular (área visível) | Colaborador | UC-08 | RF-013, RF-015, RF-018, RNF-013, RNF-027 |
| T-51 | [ver](../prototipacao/telas/T-51.jpg) | Dar feedback – celular (página inteira) | Colaborador | UC-08 | RF-013, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RN-002, RNF-012, RNF-013, RNF-027 |
| T-52 | [ver](../prototipacao/telas/T-52.jpg) | Competências dos cargos | RH, Administrador | UC-03 | RF-005, RN-001, RN-014 |
| T-53 | [ver](../prototipacao/telas/T-53.jpg) | Competências específicas da equipe | Gestor | UC-04 | RF-006, RF-018 |
| T-54 | [ver](../prototipacao/telas/T-54.jpg) | Retenção e finalidades | Administrador | UC-28 | RF-054, RF-062, RN-011, RN-012 |


Telas por caso de uso:

| Caso de uso | Telas |
|---|---|
| UC-01 Manter colaboradores e estrutura | T-44 |
| UC-02 Importar cadastro por planilha | T-44 |
| UC-03 Manter competências dos cargos | T-52 |
| UC-04 Atribuir competências específicas | T-53 |
| UC-05 Manter questionários de avaliação | T-37 |
| UC-06 Registrar fato observado | T-42 |
| UC-07 Registrar relato de colega | — |
| UC-08 Registrar feedback | T-08, T-09, T-10, T-11, T-12, T-13, T-50, T-51 |
| UC-09 Solicitar feedback | T-06, T-43 |
| UC-10 Registrar réplica | T-26 |
| UC-11 Agendar sessão de feedback | T-13, T-46 |
| UC-12 Avaliar sessão de feedback | — |
| UC-13 Planejar ciclo de avaliação | T-28, T-29, T-30, T-31, T-32, T-33, T-34 |
| UC-14 Responder avaliação | T-14, T-15, T-16, T-17, T-18 |
| UC-15 Acompanhar e encerrar ciclo | T-28, T-35, T-36 |
| UC-16 Consolidar resultados do ciclo | T-19, T-36 |
| UC-17 Moderar resposta inadequada | T-38 |
| UC-18 Registrar check-in | — |
| UC-19 Criar plano de ação | T-13, T-20 |
| UC-20 Acompanhar plano de ação | T-21, T-22 |
| UC-21 Definir metas de desenvolvimento | T-23, T-24 |
| UC-22 Consultar meu painel de desenvolvimento | T-05, T-06, T-07, T-19, T-25, T-26, T-48, T-49 |
| UC-23 Consultar painéis da equipe e da organização | T-39, T-40 |
| UC-24 Exportar histórico de colaborador | T-27 |
| UC-25 Exercer direitos de titular | T-04, T-41 |
| UC-26 Gerenciar consentimentos | T-04, T-41 |
| UC-27 Tratar solicitações de titulares | — |
| UC-28 Configurar privacidade e retenção | T-54 |
| UC-29 Registrar incidente de segurança | — |
| UC-30 Aplicar política de retenção | — |
| UC-31 Enviar lembretes e notificações | T-47 |

Seis casos de uso não têm tela no protótipo: UC-07, UC-12, UC-18, UC-27, UC-29 e UC-30. UC-07, UC-12, UC-27 e UC-29 são de prioridade Should ou Could; UC-30 é rotina automática, sem interface; o UC-18 tem o seu requisito Must (RF-023) nas telas T-09 e T-30. O protótipo cobriu os fluxos principais pedidos no enunciado. Eles continuam rastreados pelo caso de uso e pela entidade.

### 4.2 Divergências nas anotações do protótipo

Divergências encontradas na versão 1.0 do protótipo. Em 18/11/2026 as anotações foram corrigidas no Figma conforme a última coluna, e as telas de login deixaram de citar o UC-01 no nome.

| Tela | Anotação no Figma | Correção usada na matriz | Motivo |
|---|---|---|---|
| T-01, T-02 | UC-01 | Sem caso de uso (RF-003) | O login é pré-condição de todos os casos de uso. O UC-01 é "Manter colaboradores e estrutura" (diagrama, seção 8) |
| T-03, T-10 | RNF-022 | RNF-021 | RNF-022 trata do login sem teste cognitivo. Mensagem de erro clara é RNF-021 |
| T-09 | [ver](../prototipacao/telas/T-09.jpg) | RF-022, RF-023 | RF-014 é o feedback informal. O feedback formal vinculado a ciclo é RF-022, com indicadores em RF-023 |
| T-30 | [ver](../prototipacao/telas/T-30.jpg) | RF-022, RF-023 | RF-024 são as modalidades, que estão na etapa 4 |
| T-31 | [ver](../prototipacao/telas/T-31.jpg) | RF-022 | A etapa escolhe questionário e competências do ciclo (RF-022). RF-025 é a seleção de participantes do 360° e RF-026 é a notificação |
| T-32 | [ver](../prototipacao/telas/T-32.jpg) | RF-024, RF-030 | A etapa define modalidades (RF-024) e modo de identificação (RF-030). RF-027 é responder e RF-029 é registrar quem não respondeu |
| T-33 | [ver](../prototipacao/telas/T-33.jpg) | RF-022, RF-025 | A etapa convida os avaliadores (RF-025) e define datas (RF-022). RF-028 é consultar fatos ao responder |
| T-34 | [ver](../prototipacao/telas/T-34.jpg) | RF-022, RF-026 | A revisão abre o ciclo e notifica os participantes (RF-026). O intervalo inclui RF-027 a RF-029, que não são do planejamento |
| T-35 | [ver](../prototipacao/telas/T-35.jpg) | RF-029, RF-040 | A tela mostra quem respondeu e envia lembretes. RF-030 é a configuração do modo de identificação |

As anotações das telas para celular estão corretas. A matriz acrescentou a elas o RNF-027 (interface responsiva), que é o requisito que essas telas demonstram.

---

## 5. Rastreabilidade vertical

Cada linha mostra de onde o requisito veio e onde ele é tratado. "—" indica que não há ligação; os casos sem ligação estão explicados na seção 7.

### 5.1 Requisitos funcionais

| ID | Prior. | Fontes | Origem (candidatos) | Casos de uso | Telas | Entidades |
|---|---|---|---|---|---|---|
| RF-001 | Must | Entrevista | RE-28 | UC-01 | T-44 | Cargo, Colaborador, Equipe |
| RF-002 | Should | Entrevista, Pesquisa documental | RE-28; RD-39 | UC-02 | T-44 | ImportacaoCadastro |
| RF-003 | Must | Entrevista, Pesquisa documental, BPMN AS-IS | RE-27; RD-14; RP-17 | UC-01 | T-01, T-02 | PerfilColaborador |
| RF-004 | Won't | Sistema análogo | RA-23 | — | — | — |
| RF-005 | Must | Entrevista, Questionário, Sistema análogo | RE-11; RA-17; RQ-02 | UC-03 | T-52 | CargoCompetencia, Competencia, CompetenciaAtribuida |
| RF-006 | Must | Entrevista, Sistema análogo, Enunciado | RE-11; RA-17; ESC | UC-04 | T-53 | CargoCompetencia, Competencia, CompetenciaAtribuida |
| RF-007 | Must | Entrevista, Questionário, Sistema análogo, BPMN AS-IS, Enunciado | RE-12; RA-14; RQ-02; RP-02; RP-16; ESC | UC-05 | T-37 | Pergunta, Questionario |
| RF-008 | Should | Entrevista, BPMN AS-IS | RE-12; RP-02 | UC-05 | T-37 | Pergunta, Questionario |
| RF-009 | Should | Entrevista | RE-13 | UC-05 | T-37 | Pergunta, Questionario |
| RF-010 | Could | Entrevista | RE-14 | UC-13, UC-16 | — | Feedback, Pergunta, Questionario |
| RF-011 | Must | Entrevista, Sistema análogo, BPMN AS-IS | RE-02; RA-02; RP-01; RP-11 | UC-06 | T-42 | Fato |
| RF-012 | Could | Entrevista, BPMN AS-IS | RE-05; RP-15 | UC-07 | — | Fato |
| RF-013 | Must | Entrevista, Sistema análogo, BPMN AS-IS, Enunciado | RE-01; RA-24; RP-01; RP-11; ESC | UC-08 | T-08, T-09, T-50, T-51 | Feedback, FeedbackCompetencia, FeedbackFato, MembroFeedbackEquipe |
| RF-014 | Must | Entrevista, Sistema análogo, BPMN AS-IS, Enunciado | RE-04; RA-03; RP-01; ESC | UC-08 | T-08 | Feedback, FeedbackCompetencia, FeedbackFato |
| RF-015 | Should | Entrevista, Sistema análogo, BPMN AS-IS | RE-04; RA-03; RP-11 | UC-08 | T-08, T-50, T-51 | Feedback, FeedbackCompetencia, FeedbackFato |
| RF-016 | Should | Entrevista, Sistema análogo, BPMN AS-IS | RE-03; RA-21; RP-03; RP-05 | UC-08 | T-08, T-09, T-51 | VersaoFeedback |
| RF-017 | Should | Entrevista, Questionário, Pesquisa documental, Sistema análogo, BPMN AS-IS | RE-23; RQ-03; RD-37; RA-21; RP-03; RP-05; RP-09; RP-13 | UC-08 | T-08, T-51 | — |
| RF-018 | Should | Pesquisa documental | RD-06 | UC-06, UC-08 | T-08, T-50, T-51, T-53 | — |
| RF-019 | Must | Pesquisa documental, Sistema análogo | RD-16; RA-05 | UC-08, UC-14 | T-08, T-09, T-11, T-15, T-16, T-17, T-51 | — |
| RF-020 | Should | Pesquisa documental, BPMN AS-IS | RD-09; RP-13 | UC-10 | T-25, T-26 | Replica |
| RF-021 | Must | Entrevista, Sistema análogo | RA-04; RE-11 | UC-08 | T-08, T-51 | Feedback, FeedbackCompetencia, FeedbackFato |
| RF-022 | Must | Entrevista, Questionário, Sistema análogo, Enunciado | RE-06; RA-09; RQ-01; ESC | UC-13 | T-09, T-28, T-29, T-30, T-31, T-33, T-34 | AvaliadoCiclo, CicloAvaliacao, CicloCompetencia, ObjetivoCiclo |
| RF-023 | Must | Entrevista, Sistema análogo, BPMN AS-IS | RE-07; RA-16; RP-16 | UC-13, UC-18 | T-09, T-30 | Indicador, MedicaoIndicador |
| RF-024 | Must | Entrevista, Questionário, Sistema análogo, Enunciado | RE-18; RA-10; RQ-15; ESC | UC-13 | T-32 | ModalidadeCiclo |
| RF-025 | Must | Entrevista, Sistema análogo | RE-19; RA-11 | UC-13 | T-33 | ConviteAvaliacao, ModalidadeCiclo |
| RF-026 | Should | Entrevista | E01 §29; E01 §19 | UC-13, UC-31 | T-34 | AvaliadoCiclo, CicloAvaliacao, CicloCompetencia, Notificacao, ObjetivoCiclo, PreferenciaNotificacao |
| RF-027 | Must | Entrevista, Sistema análogo, Enunciado | RE-18; RE-19; RA-10; ESC | UC-14 | T-14, T-15, T-18 | ConviteAvaliacao, ItemResposta, RespostaAvaliacao |
| RF-028 | Should | Sistema análogo, Enunciado | RA-15; ESC | UC-14 | T-15 | ItemResposta, RespostaAvaliacao |
| RF-029 | Should | Entrevista, BPMN AS-IS | RE-20; RP-06 | UC-15 | T-35 | ConviteAvaliacao |
| RF-030 | Must | Entrevista, Pesquisa documental, Sistema análogo | RA-12; RD-15; RE-33 | UC-13 | T-32 | ModalidadeCiclo |
| RF-031 | Should | Questionário, Sistema análogo | RQ-06; RA-06 | UC-09 | T-06, T-43 | DestinatarioSolicitacao, SolicitacaoFeedback |
| RF-032 | Should | Questionário | RQ-16 | UC-16 | T-19 | ResultadoConsolidado |
| RF-033 | Should | Entrevista, Questionário | RE-21; RQ-18 | UC-16 | T-19 | ResultadoConsolidado |
| RF-034 | Should | Entrevista, BPMN AS-IS | RE-22; RP-08 | UC-12 | — | Feedback, FeedbackCompetencia, FeedbackFato |
| RF-035 | Could | Sistema análogo | RA-13 | UC-17 | T-38 | ItemResposta, RegistroAuditoria, RespostaAvaliacao |
| RF-036 | Could | Sistema análogo | RA-26 | UC-18 | — | CheckIn, CheckInMeta, CheckInPlano, ConfiguracaoCheckIn |
| RF-037 | Should | Entrevista, Sistema análogo, BPMN AS-IS | RE-08; RA-08; RP-12 | UC-11, UC-31 | T-13, T-46 | Notificacao, ParticipanteSessao, PreferenciaNotificacao, SessaoFeedback |
| RF-038 | Could | Entrevista, BPMN AS-IS | RE-09; RP-12 | UC-11 | T-46 | DisponibilidadeAgenda, ParticipanteSessao, SessaoFeedback |
| RF-039 | Could | Sistema análogo | RA-08 | UC-11 | T-46 | ParticipanteSessao, SessaoFeedback |
| RF-040 | Should | Questionário, BPMN AS-IS | RQ-21; RP-06; RP-14 | UC-31 | T-35, T-47 | Notificacao, PreferenciaNotificacao |
| RF-041 | Should | Entrevista, Sistema análogo, BPMN AS-IS | RA-01; RE-06; RP-07 | UC-18 | — | CheckIn, CheckInMeta, CheckInPlano, ConfiguracaoCheckIn |
| RF-042 | Must | Entrevista, Questionário, Sistema análogo, BPMN AS-IS, Enunciado | RE-15; RA-18; RQ-07; RP-14; ESC | UC-19 | T-13, T-20 | AcaoPlano, PlanoAcao, PontoMonitoramento |
| RF-043 | Must | Entrevista, Sistema análogo, BPMN AS-IS, Enunciado | RE-16; RA-18; RP-04; RP-07; RP-14; ESC | UC-20 | T-21, T-22 | AcaoPlano, PlanoAcao, PontoMonitoramento |
| RF-044 | Should | Entrevista, Questionário | RQ-17; RE-25 | UC-23 | T-39 | AcaoPlano, PlanoAcao, PontoMonitoramento |
| RF-045 | Should | Entrevista, BPMN AS-IS | RE-17; RP-04 | UC-23 | — | AcaoPlano, PlanoAcao, PontoMonitoramento |
| RF-046 | Must | Questionário, Sistema análogo, Enunciado | RA-16; RQ-08; ESC | UC-21 | T-23, T-24 | Indicador, MedicaoIndicador, Meta |
| RF-047 | Should | Entrevista | RE-10 | UC-21 | T-23 | Meta |
| RF-048 | Must | Entrevista, Questionário, Pesquisa documental, BPMN AS-IS, Enunciado | RE-24; RQ-09; RD-47; RP-01; RP-10; RP-11; ESC | UC-22 | T-05, T-25, T-27, T-48, T-49 | Cargo, Colaborador, Equipe, MembroFeedbackEquipe |
| RF-049 | Must | Entrevista, Questionário, Sistema análogo, Enunciado | RE-24; RQ-10; RQ-19; RA-20; ESC | UC-22 | T-05, T-06, T-07, T-48, T-49 | Indicador, MedicaoIndicador, ResultadoConsolidado |
| RF-050 | Should | Entrevista, Questionário, Sistema análogo, Enunciado | RE-25; RQ-16; RQ-17; RA-20; ESC | UC-23 | T-39, T-40 | ResultadoConsolidado |
| RF-051 | Should | Pesquisa documental, BPMN AS-IS | RD-47; RP-10 | UC-24 | T-27 | — |
| RF-052 | Could | Entrevista | RE-26 | UC-23 | — | ResultadoConsolidado |
| RF-053 | Must | Pesquisa documental | RD-01 | UC-25 | T-01, T-04 | ConfiguracaoOrganizacao |
| RF-054 | Should | Pesquisa documental | RD-02 | UC-28 | T-54 | CategoriaDado, CompartilhamentoDados |
| RF-055 | Must | Questionário, Pesquisa documental | RD-04; RQ-12 | UC-26 | T-04, T-41 | Consentimento, TermoConsentimento |
| RF-056 | Must | Pesquisa documental | RD-07 | UC-25 | T-41 | SolicitacaoTitular |
| RF-057 | Must | Pesquisa documental | RD-08 | UC-25 | T-41 | SolicitacaoTitular |
| RF-058 | Must | Pesquisa documental | RD-10 | UC-25 | T-41 | RegistroAuditoria, SolicitacaoTitular |
| RF-059 | Must | Pesquisa documental | RD-11 | UC-25 | T-41 | SolicitacaoTitular |
| RF-060 | Must | Pesquisa documental | RD-12 | UC-25 | T-41 | CategoriaDado, CompartilhamentoDados |
| RF-061 | Should | Pesquisa documental | RD-13 | UC-27 | — | SolicitacaoTitular |
| RF-062 | Must | Entrevista, Pesquisa documental | RD-24; RE-36 | UC-28, UC-30 | T-54 | BloqueioLegal, CategoriaDado, CompartilhamentoDados, RegistroAuditoria |
| RF-063 | Should | Pesquisa documental | RD-26 | UC-29 | — | IncidenteSeguranca, TitularAfetado |
| RF-064 | Should | Entrevista, Pesquisa documental | RD-48; RE-35 | — | T-01 | ConfiguracaoOrganizacao |
| RF-065 | Must | Pesquisa documental | RD-58 | — | T-01, T-45 | ConfiguracaoOrganizacao |

### 5.2 Requisitos não funcionais

A coluna Casos de uso traz os casos completos que aplicam o RNF. Os RNF globais (RNF-016 a RNF-023, RNF-027, RNF-030 e RNF-031, declarados na seção 6.1) valem para todas as telas e casos de uso. Quando a linha de um deles cita casos de uso ou telas, são exemplos em que o requisito aparece nos casos completos ou no protótipo, e não o limite da aplicação. RNF de infraestrutura, como disponibilidade e backup, não se ligam a tela nem a caso de uso. Legenda da verificação, como na especificação suplementar: T = teste, I = inspeção, A = análise, D = demonstração.

| ID | Prior. | Característica | Fontes | Origem (candidatos) | Casos de uso | Telas | Esp. suplementar | Verificação |
|---|---|---|---|---|---|---|---|---|
| RNF-001 | Must | Segurança | Entrevista, Questionário, Pesquisa documental | RE-29; RQ-05; RD-14 | UC-08, UC-14, UC-19 | — | seção 8.2 | T |
| RNF-002 | Must | Segurança | Pesquisa documental, Sistema análogo | RD-22; RA-07 | UC-08, UC-14, UC-19 | — | seção 8.2 | T; I |
| RNF-003 | Should | Segurança | Pesquisa documental | RD-18 | UC-08, UC-14 | — | seção 8.2 | I; T |
| RNF-004 | Must | Segurança | Pesquisa documental | RD-19 | UC-08, UC-25 | — | seção 8.2 | A; I |
| RNF-005 | Must | Segurança | Pesquisa documental | RD-20 | UC-08, UC-13, UC-14, UC-25 | T-27, T-38 | seção 8.2 | T; I |
| RNF-006 | Should | Segurança | Pesquisa documental | RD-21 | UC-08, UC-14, UC-25 | T-02 | seção 8.2 | T |
| RNF-007 | Should | Adequação funcional | Pesquisa documental | RD-43 | — | T-05, T-07, T-19, T-39, T-49 | seção 3 | I; T |
| RNF-008 | Should | Eficiência de desempenho | Pesquisa documental | RD-31 | UC-08, UC-14 | — | seção 4.2 | T |
| RNF-009 | Should | Eficiência de desempenho | Pesquisa documental | RD-32 | UC-14 | — | seção 4.2 | T |
| RNF-010 | Should | Confiabilidade | Pesquisa documental | RD-33 | — | — | seção 7 | A; I |
| RNF-011 | Should | Confiabilidade | Pesquisa documental | RD-34 | — | — | seção 7 | T; I |
| RNF-012 | Should | Confiabilidade | Pesquisa documental | RD-35 | UC-08, UC-13, UC-14, UC-19 | T-08, T-15, T-51 | seção 7 | T |
| RNF-013 | Should | Capacidade de interação | Entrevista | RE-30 | UC-08 | T-08, T-50, T-51 | seção 6.1 | I |
| RNF-014 | Should | Capacidade de interação | Questionário | RQ-11 | UC-14 | T-15 | seção 6.1 | T |
| RNF-015 | Should | Capacidade de interação | Pesquisa documental | RD-36 | UC-08, UC-13, UC-14, UC-19 | T-11, T-17, T-36 | seção 6.1 | I; T |
| RNF-016 | Must | Capacidade de interação | Pesquisa documental, Sistema análogo | RA-25; RD-57 | UC-08, UC-25 | — | seção 6.1 | I |
| RNF-017 | Must | Capacidade de interação | Pesquisa documental | RD-50 | UC-08, UC-13, UC-14, UC-19, UC-25 | — | seção 6.2 | A; I; T |
| RNF-018 | Must | Capacidade de interação | Pesquisa documental | RD-51 | UC-08, UC-13, UC-14, UC-19, UC-25 | — | seção 6.2 | T |
| RNF-019 | Must | Capacidade de interação | Pesquisa documental | RD-52 | UC-08, UC-13, UC-14, UC-19, UC-25 | — | seção 6.2 | A; I |
| RNF-020 | Must | Capacidade de interação | Pesquisa documental | RD-53 | UC-08, UC-13, UC-14, UC-19, UC-25 | T-05, T-07, T-39, T-49 | seção 6.2 | I; T |
| RNF-021 | Must | Capacidade de interação | Pesquisa documental | RD-54 | UC-08, UC-13, UC-14, UC-19, UC-25 | T-03, T-10 | seção 6.2 | I; T |
| RNF-022 | Must | Capacidade de interação | Pesquisa documental | RD-55 | UC-08, UC-13, UC-14, UC-19, UC-25 | T-01 | seção 6.2 | T |
| RNF-023 | Must | Capacidade de interação | Pesquisa documental | RD-57 | UC-08, UC-13, UC-14, UC-19, UC-25 | — | seção 6.2 | A; T |
| RNF-024 | Could | Proteção | Pesquisa documental | RD-38 | UC-08, UC-14, UC-19 | T-12 | seção 11 | T |
| RNF-025 | Won't | Compatibilidade | Pesquisa documental | RD-39 | — | — | seção 5 | D |
| RNF-026 | Should | Manutenibilidade | Pesquisa documental | RD-40 | UC-13 | — | seção 9 | D |
| RNF-027 | Must | Flexibilidade | Questionário, Pesquisa documental, Enunciado | RD-56; RQ-20; ESC | UC-08, UC-13, UC-14, UC-19, UC-25 | T-48, T-49, T-50, T-51 | seção 10 | T |
| RNF-028 | Must | Flexibilidade | Pesquisa documental, Enunciado | RD-41; ESC | — | — | seção 10 | I; A |
| RNF-029 | Should | Flexibilidade | Pesquisa documental | RD-42 | — | — | seção 10 | T |
| RNF-030 | Must | Restrição de plataforma | Enunciado | ESC | UC-08, UC-19, UC-25 | — | seção 12.1 | D; T |
| RNF-031 | Must | Restrição legal | Enunciado | ESC | UC-25 | — | seção 12.1 | A |
| RNF-032 | Must | Restrição legal | Pesquisa documental | RD-25 | — | — | seção 12.1 | I |
| RNF-033 | Must | Restrição legal | Pesquisa documental | RD-28 | — | — | seção 12.1 | I |
| RNF-034 | Should | Restrição legal | Pesquisa documental | RD-30 | — | — | seção 12.1 | I |
| RNF-035 | Won't | Restrição de plataforma | Sistema análogo | RA-22 | — | — | seção 12.1 | D |
| RNF-036 | Won't | Restrição legal | Pesquisa documental | RD-59 | — | — | seção 12.1 | A; I |

### 5.3 Regras de negócio

| ID | Prior. | Fontes | Origem (candidatos) | Casos de uso | Telas | Entidades | Esp. suplementar |
|---|---|---|---|---|---|---|---|
| RN-001 | Must | Entrevista, Pesquisa documental, Sistema análogo, Enunciado | RE-31; RD-44; RA-24; ESC | UC-05, UC-06, UC-08, UC-13, UC-14, UC-19 | T-08, T-10, T-37, T-52 | Fato, Pergunta, Questionario | — |
| RN-002 | Must | Entrevista, Sistema análogo | RA-24; RE-01 | UC-08 | T-08, T-10, T-51 | Feedback, FeedbackCompetencia, FeedbackFato | — |
| RN-003 | Must | Entrevista, Pesquisa documental | RE-32; RD-47 | UC-08, UC-17, UC-25 | T-08, T-11, T-25, T-26, T-38 | VersaoFeedback | RNF-015 (confirmação antes do envio) |
| RN-004 | Must | Entrevista, Questionário, Pesquisa documental, BPMN AS-IS, Enunciado | RE-33; RD-15; RQ-04; RQ-13; RP-17; ESC | UC-08, UC-13, UC-14, UC-25 | T-08, T-09, T-15, T-16, T-26, T-32 | Feedback, FeedbackCompetencia, FeedbackFato, ModalidadeCiclo, VinculoConfidencial | Seções 8.1 e 8.3 |
| RN-005 | Must | Questionário, Pesquisa documental, Sistema análogo | RQ-14; RD-17; RA-19 | UC-13, UC-14, UC-16, UC-23, UC-25 | T-15, T-16, T-19, T-32, T-36, T-39, T-40 | ConfiguracaoOrganizacao, ResultadoConsolidado | Seção 8.3 |
| RN-006 | Must | Entrevista, Questionário | RQ-08; RE-15 | UC-08, UC-19, UC-21 | T-20, T-22, T-24 | AcaoPlano, PlanoAcao, PontoMonitoramento | — |
| RN-007 | Must | Entrevista, Pesquisa documental, BPMN AS-IS | RE-34; RD-46; RP-10 | UC-13, UC-19, UC-23 | T-19 | — | — |
| RN-008 | Must | Pesquisa documental | RD-27 | UC-13, UC-16, UC-19, UC-22 | T-19 | ResultadoConsolidado | RNF-007 |
| RN-009 | Must | Entrevista, Pesquisa documental | RE-35; RD-48 | — | T-01 | — | — |
| RN-010 | Should | Entrevista, Pesquisa documental | RE-37; RD-23 | — | — | ConfiguracaoOrganizacao | Seção 12.1 e RNF-029 |
| RN-011 | Should | Entrevista, Pesquisa documental | RE-36; RD-24 | UC-25, UC-28, UC-30 | T-54 | ConfiguracaoOrganizacao | RNF-011 (backups), RNF-005 (trilha de auditoria) |
| RN-012 | Must | Questionário, Pesquisa documental | RD-03; RQ-12 | UC-25, UC-26 | T-04, T-54 | Consentimento, TermoConsentimento | — |
| RN-013 | Must | Pesquisa documental | RD-05 | UC-01, UC-08, UC-19 | — | Cargo, Colaborador, Equipe | — |
| RN-014 | Must | Pesquisa documental | RD-45 | UC-03, UC-05, UC-13 | T-37, T-52 | CargoCompetencia, Competencia, CompetenciaAtribuida | — |
| RN-015 | Should | Pesquisa documental | RD-49 | UC-19 | — | — | — |
| RN-016 | Must | Pesquisa documental | RD-29 | UC-01 | — | Cargo, Colaborador, CompartilhamentoDados, Equipe | — |

---

## 6. Rastreabilidade horizontal

Liga requisitos do mesmo nível. Três tipos de ligação:

- **Requisitos citados na lista geral:** o texto ou as observações do requisito citam o outro, como RF-015, que exige os campos obrigatórios de RN-002. A ligação vale nos dois sentidos.
- **RN e RNF aplicáveis:** regras e requisitos não funcionais que restringem o RF por estarem no mesmo caso de uso ou na mesma tela, ou por ligação explícita na lista geral ou na especificação suplementar.
- **Conflitos e pontos decididos:** conflitos resolvidos na lista geral (C-xx, seção 8) e pontos decididos na consolidação (P-xx, seção 9). Se uma dessas decisões mudar, todos os requisitos da linha precisam ser revistos (gestão de mudanças do processo, seção 9).

### 6.1 Requisitos funcionais

**RNF globais.** RNF-016 a RNF-023 (idioma e acessibilidade), RNF-027 (interface responsiva), RNF-030 (aplicação web) e RNF-031 (LGPD) se aplicam a todos os requisitos funcionais. Eles são declarados só aqui e não aparecem na coluna "RN e RNF aplicáveis", que traz apenas as regras específicas de cada requisito. Na seção 6.2, a coluna "RF afetados" desses RNF indica "Todos". Por isso, o RF-065 (declaração de acessibilidade), atendido pelo RNF-017, não tem RNF específico na sua linha.

| ID | Requisitos citados na lista geral | RN e RNF aplicáveis | Conflitos e pontos decididos |
|---|---|---|---|
| RF-001 | RNF-001 | RN-013, RN-016 | — |
| RF-002 | RNF-025 | — | — |
| RF-003 | RF-024, RF-061, RF-063, RNF-001, RN-004 | RNF-006, RN-009, RN-013, RN-016 | C-14 |
| RF-004 | — | — | C-11 |
| RF-005 | — | RN-014 | — |
| RF-006 | — | — | — |
| RF-007 | — | RN-001, RN-014 | — |
| RF-008 | — | RN-001, RN-014 | C-02 |
| RF-009 | — | RN-001, RN-014 | — |
| RF-010 | RN-008 | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | — |
| RF-011 | — | RN-001 | C-05 |
| RF-012 | RN-001 | RN-001 | P-06 |
| RF-013 | RN-002 | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-014 | — | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-015 | RN-002 | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | C-04 |
| RF-016 | — | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-017 | RNF-024 | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-018 | — | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-019 | RN-004 | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-009, RNF-012, RNF-013, RNF-014, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-005, RN-006, RN-013 | — |
| RF-020 | — | RN-003, RN-004 | — |
| RF-021 | RF-049 | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-024, RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 | — |
| RF-022 | RF-041 | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | C-02 |
| RF-023 | RF-041 | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | C-10 |
| RF-024 | RF-003 | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | — |
| RF-025 | — | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | C-01 |
| RF-026 | — | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | — |
| RF-027 | — | RNF-001, RNF-002, RNF-003, RNF-005, RNF-006, RNF-008, RNF-009, RNF-012, RNF-014, RNF-015, RNF-024, RN-001, RN-004, RN-005 | — |
| RF-028 | — | RNF-001, RNF-002, RNF-003, RNF-005, RNF-006, RNF-008, RNF-009, RNF-012, RNF-014, RNF-015, RNF-024, RN-001, RN-004, RN-005 | — |
| RF-029 | — | RN-004 | — |
| RF-030 | RN-004 | RNF-005, RNF-012, RNF-015, RNF-026, RN-001, RN-004, RN-005, RN-007, RN-008, RN-014 | P-01 |
| RF-031 | — | — | — |
| RF-032 | — | RNF-007, RN-005, RN-007, RN-008 | — |
| RF-033 | — | RNF-007, RN-005, RN-007, RN-008 | — |
| RF-034 | — | — | — |
| RF-035 | RN-003 | RNF-005, RN-003 | P-07 |
| RF-036 | — | — | — |
| RF-037 | RF-038, RF-040 | — | C-09, C-12 |
| RF-038 | RF-037 | — | C-12 |
| RF-039 | — | — | — |
| RF-040 | RF-037 | — | C-09 |
| RF-041 | RF-022, RF-023 | — | P-09 |
| RF-042 | RN-006 | RNF-001, RNF-002, RNF-012, RNF-015, RNF-024, RN-001, RN-004, RN-006, RN-007, RN-008, RN-013, RN-015 | — |
| RF-043 | — | RN-006 | — |
| RF-044 | — | RNF-001, RNF-007, RN-005, RN-007 | — |
| RF-045 | — | RNF-001, RN-005, RN-007 | — |
| RF-046 | RN-006 | RN-006 | — |
| RF-047 | — | RN-006 | — |
| RF-048 | — | RNF-001, RNF-005, RNF-007, RN-003, RN-008 | — |
| RF-049 | RF-021, RNF-007, RNF-020 | RNF-001, RNF-007, RN-005, RN-008 | — |
| RF-050 | RN-005 | RNF-001, RNF-007, RN-005, RN-007 | — |
| RF-051 | — | RNF-001, RNF-005 | — |
| RF-052 | — | RN-005, RN-007 | P-08 |
| RF-053 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-009, RN-011, RN-012 | — |
| RF-054 | — | RN-011 | — |
| RF-055 | RN-012 | RN-012 | C-06 |
| RF-056 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-011, RN-012 | C-13 |
| RF-057 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-011, RN-012 | — |
| RF-058 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-011, RN-012 | — |
| RF-059 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-011, RN-012 | — |
| RF-060 | — | RNF-004, RNF-005, RNF-006, RN-003, RN-004, RN-005, RN-011, RN-012 | — |
| RF-061 | RF-003 | — | — |
| RF-062 | RN-011 | RN-011 | P-05 |
| RF-063 | RF-003 | — | — |
| RF-064 | RN-009 | RN-009 | — |
| RF-065 | — | RN-009 | — |

### 6.2 Requisitos não funcionais e regras de negócio

| ID | Requisitos citados na lista geral | RF afetados | Conflitos e pontos decididos |
|---|---|---|---|
| RNF-001 | RF-001, RF-003, RNF-002, RN-005 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028, RF-042, RF-044, RF-045, RF-048, RF-049, RF-050, RF-051 | C-03, P-02 |
| RNF-002 | RNF-001 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028, RF-042 | — |
| RNF-003 | — | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028 | — |
| RNF-004 | — | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | — |
| RNF-005 | — | RF-010, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-030, RF-035, RF-048, RF-051, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | — |
| RNF-006 | — | RF-003, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | — |
| RNF-007 | RF-049 | RF-032, RF-033, RF-044, RF-048, RF-049, RF-050 | — |
| RNF-008 | RNF-009 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028 | P-10 |
| RNF-009 | RNF-008 | RF-019, RF-027, RF-028 | P-10 |
| RNF-010 | — | — | P-10 |
| RNF-011 | — | — | P-10 |
| RNF-012 | — | RF-010, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-030, RF-042 | — |
| RNF-013 | RN-002 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021 | P-10 |
| RNF-014 | — | RF-019, RF-027, RF-028 | — |
| RNF-015 | RN-003 | RF-010, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-030, RF-042 | — |
| RNF-016 | — | Todos (RNF global, seção 6.1) | — |
| RNF-017 | RNF-018, RNF-019, RNF-020, RNF-021, RNF-022, RNF-023 | Todos (RNF global, seção 6.1) | — |
| RNF-018 | RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-019 | RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-020 | RF-049, RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-021 | RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-022 | RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-023 | RNF-017 | Todos (RNF global, seção 6.1) | — |
| RNF-024 | RF-017 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-027, RF-028, RF-042 | — |
| RNF-025 | RF-002 | — | C-11 |
| RNF-026 | — | RF-010, RF-022, RF-023, RF-024, RF-025, RF-026, RF-030 | — |
| RNF-027 | — | Todos (RNF global, seção 6.1) | C-08 |
| RNF-028 | RNF-035 | — | — |
| RNF-029 | RN-010 | — | C-07 |
| RNF-030 | — | Todos (RNF global, seção 6.1) | — |
| RNF-031 | — | Todos (RNF global, seção 6.1) | — |
| RNF-032 | — | — | — |
| RNF-033 | — | — | — |
| RNF-034 | — | — | — |
| RNF-035 | RNF-028 | — | C-08 |
| RNF-036 | — | — | — |
| RN-001 | RF-012 | RF-007, RF-008, RF-009, RF-010, RF-011, RF-012, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-030, RF-042 | — |
| RN-002 | RF-013, RF-015, RNF-013 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021 | C-04 |
| RN-003 | RF-035, RNF-015 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-020, RF-021, RF-035, RF-048, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | P-04 |
| RN-004 | RF-003, RF-019, RF-030 | RF-010, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-020, RF-021, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-029, RF-030, RF-042, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | C-13, C-14, P-01 |
| RN-005 | RF-050, RNF-001 | RF-010, RF-019, RF-022, RF-023, RF-024, RF-025, RF-026, RF-027, RF-028, RF-030, RF-032, RF-033, RF-044, RF-045, RF-049, RF-050, RF-052, RF-053, RF-056, RF-057, RF-058, RF-059, RF-060 | P-03 |
| RN-006 | RF-042, RF-046 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-042, RF-043, RF-046, RF-047 | — |
| RN-007 | — | RF-010, RF-022, RF-023, RF-024, RF-025, RF-026, RF-030, RF-032, RF-033, RF-042, RF-044, RF-045, RF-050, RF-052 | — |
| RN-008 | RF-010 | RF-010, RF-022, RF-023, RF-024, RF-025, RF-026, RF-030, RF-032, RF-033, RF-042, RF-048, RF-049 | — |
| RN-009 | RF-064 | RF-003, RF-053, RF-064, RF-065 | — |
| RN-010 | RNF-029 | — | C-07 |
| RN-011 | RF-062 | RF-053, RF-054, RF-056, RF-057, RF-058, RF-059, RF-060, RF-062 | P-05 |
| RN-012 | RF-055 | RF-053, RF-055, RF-056, RF-057, RF-058, RF-059, RF-060 | C-06 |
| RN-013 | — | RF-001, RF-003, RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RF-042 | — |
| RN-014 | — | RF-005, RF-007, RF-008, RF-009, RF-010, RF-022, RF-023, RF-024, RF-025, RF-026, RF-030 | — |
| RN-015 | — | RF-042 | — |
| RN-016 | — | RF-001, RF-003 | — |

---

## 7. Verificação de cobertura

| Verificação | Resultado |
|---|---|
| Requisitos com pelo menos uma fonte | **117 de 117**. 48 requisitos são confirmados por duas ou mais técnicas de elicitação independentes: entrevista, questionário, pesquisa documental e sistema análogo. O BPMN AS-IS (seção 3) e o enunciado não entram na contagem. A seção 3 da lista geral chega a 53 porque conta o BPMN como entrevista e o enunciado como fonte |
| RF com caso de uso | 62 de 65. Sem caso de uso: RF-004 (Won't), RF-064 e RF-065 (elementos fixos da interface, presentes nas telas T-01 e T-45) |
| RF com entidade | 60 de 65. Sem entidade: RF-004 (Won't); RF-017, RF-018 e RF-019 (orientações e avisos da interface, sem dado próprio); RF-051 (relatório gerado a partir do histórico já guardado) |
| RF com tela | 55 de 65. Sem tela: 10, todos de prioridade Should, Could ou Won't (seção 5.1) |
| RNF na especificação suplementar | **36 de 36**, cada um com característica e método de verificação |
| RN com artefato | **16 de 16**. 14 têm caso de uso, 13 têm entidade, 12 têm tela. RN-009 aparece no login (T-01) e em RF-064; RN-010 está na entidade `ConfiguracaoOrganizacao` e na seção 12.1 da especificação suplementar |
| Telas com requisito | **54 de 54** (50 web e 4 para celular) |
| Requisito sem nenhum artefato | Apenas **RF-004**, que é Won't nesta versão |

**Conclusão.** Nenhum requisito ficou sem origem. O único requisito sem artefato é o RF-004, que está fora desta versão por decisão registrada (lista geral, C-11). Todos os requisitos funcionais Must aparecem em pelo menos uma tela. Os que ficaram sem tela são Should, Could ou Won't.

---

## 8. Pendências encontradas

| # | Pendência | Artefato afetado | Sugestão | Situação na revisão final (#55) |
|---|---|---|---|---|
| 1 | As anotações de 9 telas citam requisitos errados (seção 4.2) | Protótipo (#50) | Corrigir as anotações no Figma | Resolvida em 18/11/2026. As 9 anotações foram corrigidas no Figma, e as demais foram completadas com todos os requisitos da seção 4.1 |
| 2 | RF-005 e RF-006 (competências do cargo e específicas) e RF-062 (retenção) são Must e não têm tela | Protótipo (#50) | Desenhar as telas de UC-03, UC-04 e UC-28, ou registrar que ficam para a etapa de design | Resolvida em 18/11/2026. Telas T-52 (UC-03), T-53 (UC-04) e T-54 (UC-28) |
| 3 | Três decisões dos casos de uso completos pedem mudanças que ainda não estão no modelo ER: aviso `FEEDBACK_RECEBIDO` (UC08-D01; a tela T-47 já mostra esse aviso), `observado_equipe_id` em `Fato` (UC08-D02) e a confirmação do plano pelo receptor (UC19-D01) | Modelo ER (#52) | Aplicar no modelo ER e na seção 12 dele | Resolvida. Aplicadas na versão 1.1 do modelo ER (seção 14 dele), junto com os ajustes do Apêndice C.2 da especificação IEEE 830 |
| 4 | Os pontos P-01 a P-10 são decisões do grupo ainda não confirmadas pela PO | Lista geral (#45) | Ao receber a resposta da PO, usar a seção 6 desta matriz para achar todos os requisitos afetados | Aberta. Os dez pontos são decisões do grupo, ainda não confirmadas pela PO (seção 9 da lista geral) |

---

## 9. Como manter a matriz

As tabelas desta página e o CSV foram montados a partir dos artefatos listados na seção 3. Quando um deles mudar:

1. Atualize o artefato de origem (lista geral, diagrama, protótipo, modelo ER ou especificação suplementar).
2. Atualize a linha do requisito afetado aqui e no CSV, nas colunas correspondentes.
3. Se surgir uma tela nova, dê a ela o próximo número livre (`T-55` em diante) e inclua-a no catálogo da seção 4.1. Números de tela, como os de requisito, não são reutilizados.
4. Refaça a verificação da seção 7.
