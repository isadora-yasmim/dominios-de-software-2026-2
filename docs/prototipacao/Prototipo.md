# Protótipo de telas

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (INF0296, 2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #50 · **Versão:** 1.3 · **Data:** 18/11/2026
**Responsáveis:** Júlia de Souza Nascimento e Verônica Ribeiro Oliveira Palmeira
**Ferramenta:** Figma
**Base:** [Lista Geral de Requisitos](../Lista_Geral_Requisitos.md) (#45) e [Diagrama de Casos de Uso](../modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) (#47)

## Histórico de revisões

| Versão | Data | Descrição | Autora |
|---|---|---|---|
| 1.0 | 17/11/2026 | Registro do link e do escopo do protótipo | Júlia de Souza Nascimento |
| 1.1 | 17/11/2026 | Revisão final (#55): quantidade de telas e fluxos, com a numeração `T-xx` da matriz | Verônica Ribeiro Oliveira Palmeira |
| 1.2 | 18/11/2026 | Cabeçalho padronizado; seção sobre o papel do protótipo e as limitações conhecidas | Verônica Ribeiro Oliveira Palmeira |
| 1.3 | 18/11/2026 | Telas T-52 a T-54 (UC-03, UC-04, UC-28); anotações corrigidas no Figma; refinamento visual (seção 3); telas exportadas para [`telas/`](telas/) e galeria (seção 5) | Verônica Ribeiro Oliveira Palmeira |

## Sumário

1. [Acesso](#1-acesso)
2. [Escopo](#2-escopo)
3. [Padrão visual](#3-padrão-visual)
4. [Telas por fluxo](#4-telas-por-fluxo)
5. [Galeria das telas](#5-galeria-das-telas)
6. [Papel no processo de requisitos](#6-papel-no-processo-de-requisitos)

## 1. Acesso

[Abrir o protótipo no Figma](https://www.figma.com/design/yiyjqLFpIp838MAi9x0EW4/Dom%C3%ADnios-de-Software-2026-2?node-id=6-3)

O arquivo **Domínios de Software 2026-2** é a fonte do protótipo. Ele tem as páginas Capa, Componentes (sistema visual e componentes), Desktop (telas web, cada uma com a anotação dos requisitos atendidos), Mobile e Fluxos (mapa dos fluxos navegáveis). Para que as telas possam ser vistas sem acesso ao Figma, cada uma foi exportada para a pasta [`telas/`](telas/), com o identificador `T-xx` da [matriz de rastreabilidade](../Matriz_Rastreabilidade.md) (#49, seção 4).

## 2. Escopo

O protótipo representa os principais fluxos previstos para o sistema, chamado nas telas de **Trilha**:

- login e aviso de tratamento de dados (LGPD);
- painel do colaborador, com evolução, gráficos e tendências;
- emissão de feedback formal e informal, positivo e construtivo, e as modalidades gestor, pares, equipe, ascendente, autoavaliação e 360°;
- resposta a questionários de avaliação, nos modos confidencial e anônimo;
- resultado consolidado com proteção do anonimato;
- plano de ação, metas de desenvolvimento e histórico de feedbacks;
- administração de ciclos, questionários, competências e retenção de dados;
- versão para celular.

Este artefato documenta o protótipo. Ele não substitui a especificação de requisitos nem representa uma implementação funcional do sistema.

## 3. Padrão visual

O protótipo usa um sistema visual único, mantido na página Componentes do Figma, com componentes reutilizáveis (menu lateral por perfil, cabeçalho, botões, campos, status, cartões) e variáveis de cor. Em 18/11/2026 o padrão foi refinado para um visual mais sóbrio, sem alterar o conteúdo das telas.

| Elemento | Padrão |
|---|---|
| Cor de destaque | Índigo `#4F46E5`, a única cor de ação, ligada à variável `cor/primaria` |
| Textos e superfícies | Escala de cinzas: texto `#0F172A`, texto secundário `#475569`, divisórias `#E2E8F0`, fundo `#F8FAFC`. Menu lateral e painel do login em grafite `#0F172A` |
| Estados | Sucesso, atenção, erro e informação com cor, ícone e texto, nunca só com a cor (RNF-019) |
| Tipografia | Inter, com hierarquia de título, subtítulo e corpo |
| Forma | Cantos de 12 px nos cartões e 8 px em campos, botões e elementos internos; sombra discreta nos cartões; sem degradês |
| Acessibilidade | Contraste conferido pela fórmula das WCAG 2.2: cor de destaque 6,3:1 sobre branco, texto secundário 7,6:1, contorno de campos 4,8:1, texto do menu 12,0:1 sobre o grafite (RNF-017, RNF-019). Foco visível, alvos de toque de no mínimo 24 × 24 px no celular (RNF-027) |

## 4. Telas por fluxo

O protótipo tem **54 telas**: 50 na versão web e 4 na versão para celular. A coluna Requisitos de cada tela está no catálogo da [matriz](../Matriz_Rastreabilidade.md#41-catálogo-das-telas) e na anotação da tela no Figma.

| Fluxo | O que mostra | Telas |
|---|---|---|
| Acesso e LGPD | Login, verificação em duas etapas, erro de login e aviso de tratamento de dados no primeiro acesso | T-01, T-02, T-03, T-04 |
| Painel do colaborador | Evolução por competência, estado vazio e alternativa em tabela para o gráfico | T-05, T-06, T-07 |
| Dar feedback | Formal e informal, positivo e construtivo, com fato obrigatório, confirmação e alerta de termo ofensivo | T-08, T-09, T-10, T-11, T-12, T-13 |
| Responder avaliação | Modos confidencial e anônimo, confirmação e envio | T-14, T-15, T-16, T-17, T-18 |
| Resultado do ciclo | Resultado consolidado com mínimo de respondentes e comparação com a autoavaliação | T-19 |
| Plano de ação, metas e histórico | Plano de ação, acompanhamento, metas, feedbacks recebidos e enviados, réplica e visão do RH | T-20, T-21, T-22, T-23, T-24, T-25, T-26, T-27 |
| Ciclos de avaliação, questionários e moderação | Planejamento em 6 etapas, acompanhamento, encerramento, questionários e moderação | T-28, T-29, T-30, T-31, T-32, T-33, T-34, T-35, T-36, T-37, T-38 |
| Painéis da equipe e da organização | Indicadores consolidados, com mínimo de respondentes | T-39, T-40 |
| Telas complementares | Direitos do titular, registro de fato, pedido de feedback, cadastro, acessibilidade, sessão e notificações | T-41, T-42, T-43, T-44, T-45, T-46, T-47 |
| Competências e retenção de dados | Competências do cargo, competências específicas e política de retenção (telas criadas em 18/11/2026) | T-52, T-53, T-54 |
| Versão para celular | Painel e feedback informal em 390 px, área visível e página inteira | T-48, T-49, T-50, T-51 |

## 5. Galeria das telas

Clique na imagem para abrir em tamanho real. Cada legenda traz o perfil, o caso de uso e os requisitos atendidos.

### Acesso e LGPD

**T-01 · Entrar (login)** · Todos · sem caso de uso · RF-003, RNF-022, RF-053, RF-064, RF-065, RN-009

<a href="telas/T-01.jpg"><img src="telas/T-01.jpg" width="720" alt="T-01 – Entrar (login)"></a>

**T-02 · Verificação em duas etapas** · RH, Administrador · sem caso de uso · RF-003, RNF-006

<a href="telas/T-02.jpg"><img src="telas/T-02.jpg" width="720" alt="T-02 – Verificação em duas etapas"></a>

**T-03 · Entrar – erro de login** · Todos · sem caso de uso · RNF-021

<a href="telas/T-03.jpg"><img src="telas/T-03.jpg" width="720" alt="T-03 – Entrar – erro de login"></a>

**T-04 · Primeiro acesso – como tratamos seus dados** · Colaborador · UC-25, UC-26 · RF-053, RF-055, RN-012

<a href="telas/T-04.jpg"><img src="telas/T-04.jpg" width="720" alt="T-04 – Primeiro acesso – como tratamos seus dados"></a>

### Painel do colaborador

**T-05 · Início – painel do colaborador** · Colaborador · UC-22 · RF-048, RF-049, RNF-007, RNF-020

<a href="telas/T-05.jpg"><img src="telas/T-05.jpg" width="720" alt="T-05 – Início – painel do colaborador"></a>

**T-06 · Início – sem feedbacks (estado vazio)** · Colaborador · UC-22, UC-09 · RF-049, RF-031

<a href="telas/T-06.jpg"><img src="telas/T-06.jpg" width="720" alt="T-06 – Início – sem feedbacks (estado vazio)"></a>

**T-07 · Evolução por competência – dados em tabela** · Colaborador · UC-22 · RF-049, RNF-007, RNF-020

<a href="telas/T-07.jpg"><img src="telas/T-07.jpg" width="720" alt="T-07 – Evolução por competência – dados em tabela"></a>

### Dar feedback

**T-08 · Dar feedback – informal** · Colaborador · UC-08 · RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RN-001, RN-002, RN-003, RN-004, RNF-012, RNF-013

<a href="telas/T-08.jpg"><img src="telas/T-08.jpg" width="720" alt="T-08 – Dar feedback – informal"></a>

**T-09 · Dar feedback – formal (ciclo)** · Gestor · UC-08 · RF-013, RF-016, RF-019, RF-022, RF-023, RN-004

<a href="telas/T-09.jpg"><img src="telas/T-09.jpg" width="720" alt="T-09 – Dar feedback – formal (ciclo)"></a>

**T-10 · Dar feedback – erro: nenhum fato vinculado** · Colaborador · UC-08 · RN-001, RN-002, RNF-021

<a href="telas/T-10.jpg"><img src="telas/T-10.jpg" width="720" alt="T-10 – Dar feedback – erro: nenhum fato vinculado"></a>

**T-11 · Dar feedback – confirmar envio** · Colaborador · UC-08 · RF-019, RN-003, RNF-015

<a href="telas/T-11.jpg"><img src="telas/T-11.jpg" width="720" alt="T-11 – Dar feedback – confirmar envio"></a>

**T-12 · Dar feedback – alerta de termo ofensivo** · Colaborador · UC-08 · RNF-024

<a href="telas/T-12.jpg"><img src="telas/T-12.jpg" width="720" alt="T-12 – Dar feedback – alerta de termo ofensivo"></a>

**T-13 · Feedback enviado** · Colaborador · UC-08, UC-11, UC-19 · RF-037, RF-042

<a href="telas/T-13.jpg"><img src="telas/T-13.jpg" width="720" alt="T-13 – Feedback enviado"></a>

### Responder avaliação

**T-14 · Avaliações pendentes** · Avaliador convidado · UC-14 · RF-027

<a href="telas/T-14.jpg"><img src="telas/T-14.jpg" width="720" alt="T-14 – Avaliações pendentes"></a>

**T-15 · Responder avaliação – modo confidencial** · Avaliador convidado · UC-14 · RF-019, RF-027, RF-028, RN-004, RN-005, RNF-012, RNF-014

<a href="telas/T-15.jpg"><img src="telas/T-15.jpg" width="720" alt="T-15 – Responder avaliação – modo confidencial"></a>

**T-16 · Responder avaliação – modo anônimo** · Avaliador convidado · UC-14 · RF-019, RN-004, RN-005

<a href="telas/T-16.jpg"><img src="telas/T-16.jpg" width="720" alt="T-16 – Responder avaliação – modo anônimo"></a>

**T-17 · Responder avaliação – confirmar envio** · Avaliador convidado · UC-14 · RF-019, RNF-015

<a href="telas/T-17.jpg"><img src="telas/T-17.jpg" width="720" alt="T-17 – Responder avaliação – confirmar envio"></a>

**T-18 · Avaliações – após o envio** · Avaliador convidado · UC-14 · RF-027

<a href="telas/T-18.jpg"><img src="telas/T-18.jpg" width="720" alt="T-18 – Avaliações – após o envio"></a>

### Resultado do ciclo

**T-19 · Resultado do ciclo** · Colaborador · UC-16, UC-22 · RF-032, RF-033, RN-005, RN-007, RN-008, RNF-007

<a href="telas/T-19.jpg"><img src="telas/T-19.jpg" width="720" alt="T-19 – Resultado do ciclo"></a>

### Plano de ação, metas e histórico

**T-20 · Novo plano de ação** · Gestor · UC-19 · RF-042, RN-006

<a href="telas/T-20.jpg"><img src="telas/T-20.jpg" width="720" alt="T-20 – Novo plano de ação"></a>

**T-21 · Acompanhar plano de ação** · Colaborador · UC-20 · RF-043

<a href="telas/T-21.jpg"><img src="telas/T-21.jpg" width="720" alt="T-21 – Acompanhar plano de ação"></a>

**T-22 · Plano de ação – data final** · Gestor · UC-20 · RF-043, RN-006

<a href="telas/T-22.jpg"><img src="telas/T-22.jpg" width="720" alt="T-22 – Plano de ação – data final"></a>

**T-23 · Metas e planos de ação** · Colaborador · UC-21 · RF-046, RF-047

<a href="telas/T-23.jpg"><img src="telas/T-23.jpg" width="720" alt="T-23 – Metas e planos de ação"></a>

**T-24 · Nova meta** · Colaborador · UC-21 · RF-046, RN-006

<a href="telas/T-24.jpg"><img src="telas/T-24.jpg" width="720" alt="T-24 – Nova meta"></a>

**T-25 · Feedbacks recebidos e enviados** · Colaborador · UC-22 · RF-048, RF-020, RN-003

<a href="telas/T-25.jpg"><img src="telas/T-25.jpg" width="720" alt="T-25 – Feedbacks recebidos e enviados"></a>

**T-26 · Detalhe do feedback, com versões e réplica** · Colaborador · UC-10, UC-22 · RF-020, RN-003, RN-004

<a href="telas/T-26.jpg"><img src="telas/T-26.jpg" width="720" alt="T-26 – Detalhe do feedback, com versões e réplica"></a>

**T-27 · Histórico do colaborador – visão do RH** · RH · UC-24 · RF-048, RF-051, RNF-005

<a href="telas/T-27.jpg"><img src="telas/T-27.jpg" width="720" alt="T-27 – Histórico do colaborador – visão do RH"></a>

### Ciclos de avaliação, questionários e moderação

**T-28 · Ciclos de avaliação** · RH, Gestor · UC-13, UC-15 · RF-022

<a href="telas/T-28.jpg"><img src="telas/T-28.jpg" width="720" alt="T-28 – Ciclos de avaliação"></a>

**T-29 · Planejar ciclo 1/6 – dados gerais** · RH, Gestor · UC-13 · RF-022

<a href="telas/T-29.jpg"><img src="telas/T-29.jpg" width="720" alt="T-29 – Planejar ciclo 1/6 – dados gerais"></a>

**T-30 · Planejar ciclo 2/6 – objetivos e indicadores** · RH, Gestor · UC-13 · RF-022, RF-023

<a href="telas/T-30.jpg"><img src="telas/T-30.jpg" width="720" alt="T-30 – Planejar ciclo 2/6 – objetivos e indicadores"></a>

**T-31 · Planejar ciclo 3/6 – competências e questionário** · RH, Gestor · UC-13 · RF-022

<a href="telas/T-31.jpg"><img src="telas/T-31.jpg" width="720" alt="T-31 – Planejar ciclo 3/6 – competências e questionário"></a>

**T-32 · Planejar ciclo 4/6 – modalidades e privacidade** · RH, Gestor · UC-13 · RF-024, RF-030, RN-004, RN-005

<a href="telas/T-32.jpg"><img src="telas/T-32.jpg" width="720" alt="T-32 – Planejar ciclo 4/6 – modalidades e privacidade"></a>

**T-33 · Planejar ciclo 5/6 – participantes e datas** · RH, Gestor · UC-13 · RF-022, RF-025

<a href="telas/T-33.jpg"><img src="telas/T-33.jpg" width="720" alt="T-33 – Planejar ciclo 5/6 – participantes e datas"></a>

**T-34 · Planejar ciclo 6/6 – revisão e abertura** · RH, Gestor · UC-13 · RF-022, RF-026

<a href="telas/T-34.jpg"><img src="telas/T-34.jpg" width="720" alt="T-34 – Planejar ciclo 6/6 – revisão e abertura"></a>

**T-35 · Acompanhar ciclo** · RH, Gestor · UC-15 · RF-029, RF-040

<a href="telas/T-35.jpg"><img src="telas/T-35.jpg" width="720" alt="T-35 – Acompanhar ciclo"></a>

**T-36 · Encerrar ciclo – confirmação** · RH, Gestor · UC-15, UC-16 · RN-005, RNF-015

<a href="telas/T-36.jpg"><img src="telas/T-36.jpg" width="720" alt="T-36 – Encerrar ciclo – confirmação"></a>

**T-37 · Competências e questionários** · RH · UC-05 · RF-007, RF-008, RF-009, RN-001, RN-014

<a href="telas/T-37.jpg"><img src="telas/T-37.jpg" width="720" alt="T-37 – Competências e questionários"></a>

**T-38 · Moderação antes de liberar resultados** · RH · UC-17 · RF-035, RN-003, RNF-005

<a href="telas/T-38.jpg"><img src="telas/T-38.jpg" width="720" alt="T-38 – Moderação antes de liberar resultados"></a>

### Painéis da equipe e da organização

**T-39 · Minha equipe – painel do gestor** · Gestor · UC-23 · RF-044, RF-050, RN-005, RNF-007, RNF-020

<a href="telas/T-39.jpg"><img src="telas/T-39.jpg" width="720" alt="T-39 – Minha equipe – painel do gestor"></a>

**T-40 · Painel da organização** · RH · UC-23 · RF-050, RN-005

<a href="telas/T-40.jpg"><img src="telas/T-40.jpg" width="720" alt="T-40 – Painel da organização"></a>

### Telas complementares

**T-41 · Meus dados (direitos do titular)** · Colaborador · UC-25, UC-26 · RF-055, RF-056, RF-057, RF-058, RF-059, RF-060

<a href="telas/T-41.jpg"><img src="telas/T-41.jpg" width="720" alt="T-41 – Meus dados (direitos do titular)"></a>

**T-42 · Registrar fato** · Colaborador · UC-06 · RF-011

<a href="telas/T-42.jpg"><img src="telas/T-42.jpg" width="720" alt="T-42 – Registrar fato"></a>

**T-43 · Pedir feedback** · Colaborador · UC-09 · RF-031

<a href="telas/T-43.jpg"><img src="telas/T-43.jpg" width="720" alt="T-43 – Pedir feedback"></a>

**T-44 · Usuários e estrutura – importação de planilha** · RH, Administrador · UC-01, UC-02 · RF-001, RF-002

<a href="telas/T-44.jpg"><img src="telas/T-44.jpg" width="720" alt="T-44 – Usuários e estrutura – importação de planilha"></a>

**T-45 · Declaração de acessibilidade** · Todos · sem caso de uso · RF-065

<a href="telas/T-45.jpg"><img src="telas/T-45.jpg" width="720" alt="T-45 – Declaração de acessibilidade"></a>

**T-46 · Agendar sessão de feedback** · Gestor · UC-11 · RF-037, RF-038, RF-039

<a href="telas/T-46.jpg"><img src="telas/T-46.jpg" width="720" alt="T-46 – Agendar sessão de feedback"></a>

**T-47 · Notificações** · Todos · UC-31 · RF-040

<a href="telas/T-47.jpg"><img src="telas/T-47.jpg" width="720" alt="T-47 – Notificações"></a>

### Competências e retenção de dados

**T-52 · Competências dos cargos** · RH, Administrador · UC-03 · RF-005, RN-001, RN-014

<a href="telas/T-52.jpg"><img src="telas/T-52.jpg" width="720" alt="T-52 – Competências dos cargos"></a>

**T-53 · Competências específicas da equipe** · Gestor · UC-04 · RF-006, RF-018

<a href="telas/T-53.jpg"><img src="telas/T-53.jpg" width="720" alt="T-53 – Competências específicas da equipe"></a>

**T-54 · Retenção e finalidades** · Administrador · UC-28 · RF-054, RF-062, RN-011, RN-012

<a href="telas/T-54.jpg"><img src="telas/T-54.jpg" width="720" alt="T-54 – Retenção e finalidades"></a>

### Versão para celular

**T-48 · Início – celular (área visível)** · Colaborador · UC-22 · RF-048, RF-049, RNF-027

<a href="telas/T-48.jpg"><img src="telas/T-48.jpg" width="300" alt="T-48 – Início – celular (área visível)"></a>

**T-49 · Início – celular (página inteira)** · Colaborador · UC-22 · RF-048, RF-049, RNF-007, RNF-020, RNF-027

<a href="telas/T-49.jpg"><img src="telas/T-49.jpg" width="300" alt="T-49 – Início – celular (página inteira)"></a>

**T-50 · Dar feedback – celular (área visível)** · Colaborador · UC-08 · RF-013, RF-015, RF-018, RNF-013, RNF-027

<a href="telas/T-50.jpg"><img src="telas/T-50.jpg" width="300" alt="T-50 – Dar feedback – celular (área visível)"></a>

**T-51 · Dar feedback – celular (página inteira)** · Colaborador · UC-08 · RF-013, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021, RN-002, RNF-012, RNF-013, RNF-027

<a href="telas/T-51.jpg"><img src="telas/T-51.jpg" width="300" alt="T-51 – Dar feedback – celular (página inteira)"></a>

## 6. Papel no processo de requisitos

O protótipo é a técnica de validação e de elicitação complementar do [processo de requisitos](../Processo_Requisitos.md) (seções 2.4 e 3, prefixo `RT`). Ele mostra como os requisitos da lista geral aparecem nas telas, nos fluxos dos casos de uso. Nenhum requisito novo surgiu na prototipação, por isso não há candidatos `RT` na lista geral.

| Ponto | Situação |
|---|---|
| Anotações de 9 telas citavam requisitos diferentes dos da lista geral | Corrigidas no Figma em 18/11/2026, conforme a [matriz](../Matriz_Rastreabilidade.md), seção 4.2. As demais anotações foram completadas com todos os requisitos da tela |
| RF-005, RF-006 e RF-062, de prioridade Must, não tinham tela | Telas T-52, T-53 e T-54, criadas em 18/11/2026 |
| Casos de uso sem tela própria | UC-07, UC-12, UC-27 e UC-29 (prioridade Should ou Could); UC-30, rotina automática sem interface; UC-18, cujo requisito Must (RF-023, registro dos indicadores) aparece nas telas T-09 e T-30. Todos continuam rastreados pelo caso de uso e pela entidade ([matriz](../Matriz_Rastreabilidade.md), seção 4.1) |
