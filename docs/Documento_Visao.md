# Documento Visão

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (INF0296, 2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #46 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Ana Luísa Pereira dos Santos
**Referência de método:** Larman, *Utilizando UML e Padrões*, cap. 7 (Documento Visão)
**Base:** [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) (issue #45), versão 1.0. Os identificadores `RF-`, `RNF-` e `RN-` citados aqui são os dessa lista.

---

## Sumário

1. [Introdução](#1-introdução)
2. [Posicionamento](#2-posicionamento)
3. [Partes interessadas e usuários](#3-partes-interessadas-e-usuários)
4. [Objetivos e necessidades](#4-objetivos-e-necessidades)
5. [Visão geral do produto](#5-visão-geral-do-produto)
6. [Resumo das funcionalidades](#6-resumo-das-funcionalidades)
7. [Restrições](#7-restrições)
8. [Pontos em aberto](#8-pontos-em-aberto)
9. [Fontes](#9-fontes)

---

## 1. Introdução

### 1.1 Finalidade

Este documento apresenta a visão geral do Sistema Web de Feedback e Gestão de Competências: que problema ele resolve, para quem, com que funções principais e dentro de que limites. É um texto curto, pensado para ser lido por todas as partes interessadas, inclusive quem não é da área técnica. O detalhe de cada requisito está na [Lista Geral de Requisitos](Lista_Geral_Requisitos.md), e os próximos artefatos (casos de uso, especificação suplementar, glossário) partem daqui.

### 1.2 Escopo

O sistema cobre o ciclo completo do feedback dentro de uma organização: registrar fatos e feedbacks (formais, informais, positivos e construtivos), coletar avaliações de gestor, pares, equipe e autoavaliação (inclusive 360°), preservar a confidencialidade de quem avalia, acompanhar planos de ação e metas de desenvolvimento, guardar o histórico e analisar os resultados com gráficos e tendências.

O sistema **não** é canal de denúncia (RN-009), **não** decide promoção, salário ou desligamento (RN-007) e **não** inclui, nesta versão, aplicativo móvel nativo nem integração com sistemas externos. A lista completa do que ficou de fora está na seção 10 da Lista Geral de Requisitos.

### 1.3 Definições

Os termos usados aqui (emissor, receptor, fato, feedback formal e informal, ciclo, check-in, modalidade, confidencial e anônimo) seguem a seção 2.4 da Lista Geral de Requisitos. O glossário completo será feito na issue #53.

---

## 2. Posicionamento

### 2.1 Oportunidade de negócio

Dar e receber feedback é parte do dia a dia de qualquer equipe, mas as organizações ouvidas no levantamento fazem isso sem apoio de ferramenta. A Product Owner (PO) descreveu um processo estruturado, porém manual (papel, planilha). A Secretaria Municipal de Educação entrevistada faz tudo por conversa, sem nenhum registro formal. Nos dois casos, o conhecimento sobre o desempenho das pessoas fica na memória de quem gerencia.

Há espaço para um sistema que torne o feedback fácil de registrar, seguro para quem avalia e acompanhável ao longo do tempo, em português e adequado à LGPD. O sistema análogo analisado (15Five) mostra que o mercado já tem esse tipo de solução, mas ela não cobre bem a realidade brasileira. Uma limitação apontada na análise é a falta de português (RNF-016).

### 2.2 Declaração do problema

| | |
|---|---|
| **O problema de** | feedback e avaliação de desempenho feitos de forma manual ou informal, sem registro confiável, sem acompanhamento e sem proteção a quem avalia |
| **afeta** | colaboradores, gestores e o RH das organizações |
| **O impacto disso é** | informação que se perde; ausência de controle sobre se a pessoa melhorou; feedback que não acontece por falta de tempo ou de agenda; reação defensiva de quem recebe; feedback dado de forma agressiva ou sem elogio; participação irregular nas avaliações 360°; dependência da discrição do gestor para proteger quem reclama |
| **Uma solução bem-sucedida seria** | um sistema web que registre fatos e feedbacks, guie quem dá e quem recebe, ligue o feedback a planos de ação com prazo e lembrete, guarde o histórico e proteja a identidade de quem avalia, tudo em conformidade com a LGPD |

As dores acima são as seis marcadas em cada um dos diagramas do processo atual (D1 a D6, ver [Processo AS-IS e dores](elicitacao/bpmn/Processo_AS-IS_e_Dores.md)). A seção 7.2 da Lista Geral de Requisitos mostra quais requisitos tratam cada uma.

### 2.3 Declaração de posição do produto

| | |
|---|---|
| **Para** | organizações, de pequenas a grandes, que querem desenvolver suas pessoas por meio de feedback |
| **que** | precisam registrar, acompanhar e analisar feedbacks e avaliações sem depender de papel, planilha ou da memória do gestor |
| **o** | Sistema Web de Feedback e Gestão de Competências |
| **é um** | sistema web de gestão de feedback e de desenvolvimento por competências |
| **que** | liga cada feedback a fatos observados, a competências e a planos de ação acompanhados até o resultado, e mantém o histórico de cada colaborador |
| **Diferentemente de** | planilhas, anotações e mensagens de aplicativos, e de ferramentas estrangeiras como o 15Five |
| **nosso produto** | exige base em fatos, oferece modos de identificação do emissor (identificado, confidencial e anônimo) com número mínimo de respondentes, funciona em português e foi pensado desde o início para a LGPD e a acessibilidade |

---

## 3. Partes interessadas e usuários

### 3.1 Perfil do mercado

O sistema atende a uma organização por instalação (RN-010), de qualquer setor. O levantamento mostrou duas realidades bem diferentes, e o sistema precisa servir às duas:

- **Organização com processo de feedback estruturado e RH.** É o caso descrito pela PO: ciclos planejados, check-ins, 360° e histórico usado pelo RH.
- **Organização pequena, sem RH próprio, com hierarquia em vários níveis.** É o caso da secretaria municipal entrevistada, em que a chefia responde a uma autoridade superior e os setores têm de 1 a 5 pessoas. Nela, um mesmo usuário acumula perfis (RF-003), com um limite que protege quem avalia (RN-004).

### 3.2 Resumo das partes interessadas

| Parte interessada | Descrição | Interesse no sistema |
|---|---|---|
| **Product Owner (Profa. Adriana)** | Representa o cliente. Definiu o processo desejado nas entrevistas e valida as decisões da Lista Geral de Requisitos | Que o sistema reflita o processo de feedback que ela descreveu e que a lista de requisitos seja ampla, como ela pediu |
| **Organização contratante** | Empresa ou órgão público que adota o sistema. É a controladora dos dados pessoais | Desenvolver pessoas, ter histórico confiável e cumprir a LGPD |
| **Colaboradores (titulares dos dados)** | As pessoas avaliadas e que também avaliam | Receber feedback justo e útil, ter seus dados protegidos e exercer seus direitos de titular |
| **Gestores** | Quem planeja ciclos, dá feedback e acompanha a equipe | Gastar menos tempo para registrar, planejar e acompanhar |
| **RH** | Quem configura o processo e usa o histórico em decisões sobre pessoas | Ter controle e informação organizada |
| **Diretoria** | Cúpula da organização | Visão agregada, sem acesso a resultados individuais (RNF-001) |
| **Encarregado de dados** | Quem atende titulares e a ANPD na organização | Ferramentas para registrar, responder e comprovar o cumprimento da LGPD (RF-054, RF-061, RF-063) |
| **Equipe de desenvolvimento** | Ana Luísa, Davi, Isadora, Júlia e Verônica, alunas e aluno de Engenharia de Software da UFG | Entregar a primeira etapa com requisitos claros, rastreáveis e validados |
| **Professora da disciplina** | Avalia o trabalho | Que o levantamento siga o enunciado e o processo definido |

### 3.3 Resumo dos usuários

| Usuário | O que faz no sistema | Requisitos principais |
|---|---|---|
| **Colaborador** | Recebe e pede feedback, responde avaliações, replica um feedback, define metas, acompanha sua evolução, exerce direitos da LGPD | RF-020, RF-031, RF-046, RF-048, RF-049, RF-056 a RF-060 |
| **Gestor** | Registra fatos, dá feedback formal e informal, planeja ciclos e check-ins, agenda sessões, constrói e acompanha planos de ação | RF-006, RF-011 a RF-016, RF-022, RF-037, RF-041 a RF-044 |
| **RH** | Cadastra competências e questionários padrão, configura modos de identificação, consulta o histórico, acompanha planos da organização | RF-001, RF-005, RF-008, RF-030, RF-044, RF-050, RF-051 |
| **Administrador** | Cadastra usuários e hierarquia, parametriza o sistema, configura retenção e finalidades dos dados | RF-001, RF-002, RF-054, RF-062, RNF-026 |
| **Diretoria** | Consulta indicadores agregados | RF-050, RNF-001 |
| **Encarregado de dados** | Atende solicitações de titulares e incidentes | RF-061, RF-063 |

Um mesmo usuário pode acumular perfis, como o gestor que também é avaliado pelo seu superior (RF-003).

### 3.4 Ambiente do usuário

- O sistema é acessado por **navegador web** (RNF-030), em computador ou celular. A interface é responsiva desde a primeira versão (RNF-027).
- A interface, as mensagens e os modelos de perguntas estão em **português do Brasil** (RNF-016).
- O sistema deve ser usável por pessoas com deficiência, conforme a ABNT NBR 17225:2025 e as WCAG 2.2 (RNF-017 a RNF-023).
- Cada avaliador deve conseguir avaliar um colega em até 20 minutos (RNF-014), e o feedback informal deve caber em uma tela (RNF-013).

---

## 4. Objetivos e necessidades

### 4.1 Objetivos do produto

1. Fazer com que o feedback aconteça e fique registrado, e não dependa da memória nem do tempo do gestor.
2. Basear todo feedback em fatos e comportamentos observados, e não em opinião (RN-001).
3. Permitir saber se uma pessoa melhorou depois de um feedback, por meio de plano de ação com prazo e acompanhamento.
4. Proteger quem avalia, para que as pessoas sejam sinceras, sem expor a identidade do emissor por descuido ou por exclusão (RN-004, RN-005).
5. Dar ao colaborador, ao gestor e ao RH uma visão da evolução por competência, com números e gráficos.
6. Servir como apoio ao desenvolvimento das pessoas, e não como instrumento de punição (RN-007, RN-008).
7. Estar em conformidade com a LGPD e com as normas de acessibilidade desde a primeira versão.

### 4.2 Necessidades principais

A tabela liga cada necessidade levantada às dores do processo atual e aos requisitos que a atendem.

| # | Necessidade | Quem precisa | Situação hoje | Requisitos |
|---|---|---|---|---|
| N1 | Registrar fatos, feedbacks e elogios de forma simples | Gestor, colaborador | Papel, Excel, caderninho, WhatsApp ou só de boca (D1) | RF-011, RF-013, RF-014, RF-015, RF-048 |
| N2 | Gastar menos tempo para planejar e dar feedback | Gestor | Planejar e acompanhar cada pessoa dá trabalho; as agendas não coincidem e o feedback passa batido (D2) | RF-007, RF-008, RF-037, RF-038, RNF-013 |
| N3 | Dar e receber feedback de forma estruturada e menos defensiva | Gestor, colaborador | Reação defensiva e feedback agressivo ou sem elogio (D3, D5) | RF-016, RF-017, RF-020, RNF-024 |
| N4 | Saber se a pessoa melhorou | Gestor, RH | Sem controle, depende da memória (D4) | RF-040, RF-042, RF-043, RF-045 |
| N5 | Garantir a participação nas avaliações | Gestor, RH | Participação no 360° não garantida (D6) | RF-029, RF-040 |
| N6 | Avaliar por critérios objetivos | Gestor, RH | Avaliação pela percepção, sem formulário nem indicadores (D6) | RF-007, RF-009, RF-023 |
| N7 | Proteger a identidade de quem avalia | Colaborador (emissor) | Depende só da discrição do gestor (D5) | RF-019, RF-030, RN-004, RN-005, RNF-001, RNF-003 |
| N8 | Consultar o histórico para decisões sobre pessoas | RH | Sem histórico, ou histórico espalhado | RF-048, RF-051, RN-003, RN-007 |
| N9 | Acompanhar a evolução por competência | Colaborador, gestor, RH | Não existe | RF-005, RF-021, RF-049, RF-050 |
| N10 | Cumprir a LGPD e a acessibilidade | Organização, encarregado | Não se aplica, pois não há sistema | RF-053 a RF-065, RNF-004, RNF-005, RNF-017, RN-012 |
| N11 | Funcionar em organização pequena, sem RH próprio | Gestor | O RH não participa do processo | RF-003, RN-004 |

---

## 5. Visão geral do produto

### 5.1 Perspectiva do produto

O sistema é uma aplicação web independente, com uma instalação por organização (RN-010). O back-end expõe todas as funções por uma API própria, separada da interface web, para que o futuro aplicativo móvel reaproveite as mesmas regras (RNF-028). Nesta versão, o cadastro de usuários é feito pela própria organização, manualmente ou por planilha (RF-001, RF-002), e não há integração com sistemas de RH ou de folha (RNF-025).

### 5.2 Resumo dos benefícios

| Benefício | Funções que o sustentam |
|---|---|
| Nenhum feedback se perde | Registro de fatos e feedbacks, histórico cronológico (RF-011, RF-013, RF-048) |
| Feedback mais justo e menos defensivo | Base em fatos, estrutura por tipo de feedback, orientações, réplica do receptor (RN-001, RF-016, RF-017, RF-020) |
| Menos trabalho para o gestor | Modelos de questionário, formulário simples, agendamento com lembrete, consolidação automática (RF-007, RF-015, RF-037, RF-032) |
| Melhoria acompanhada até o resultado | Plano de ação com prazo, monitoramento e lembretes (RF-042, RF-043, RF-040) |
| Avaliadores mais sinceros | Modos confidencial e anônimo, mínimo de respondentes (RN-004, RN-005) |
| Visão de evolução | Painéis individual, de equipe e da organização, com gráficos acessíveis (RF-049, RF-050, RNF-020) |
| Segurança jurídica | Requisitos de LGPD, trilha de auditoria, retenção configurável (RF-053 a RF-065, RNF-005) |

### 5.3 Suposições e dependências

- A organização cadastra os dados dos colaboradores, dos cargos e da hierarquia. O sistema não os obtém sozinho (RF-001, RF-002).
- A organização é a controladora dos dados pessoais, e o sistema apoia suas obrigações, como atender titulares e comunicar incidentes (RF-061, RF-063).
- A PO ainda precisa confirmar os dez pontos a validar da Lista Geral de Requisitos (seção 8 deste documento). Os requisitos já estão escritos conforme a decisão adotada.
- Se o sistema for oferecido como serviço (SaaS), valem os registros de acesso (RNF-032). Se a hospedagem for fora do Brasil, vale a regra de transferência internacional (RNF-033).

### 5.4 Custo, licenciamento e instalação

Fora do escopo desta etapa. O trabalho da disciplina não define preço, modelo de licença nem forma de instalação. Esses pontos só entrariam se o sistema fosse levado adiante como produto.

---

## 6. Resumo das funcionalidades

A lista abaixo agrupa as 65 funções (RF) em áreas. Cada linha traz as funções essenciais (Must) em destaque, quando há. O detalhe, as prioridades e as observações estão na seção 4 da Lista Geral de Requisitos.

| Área | O que o sistema faz | Requisitos |
|---|---|---|
| **Organização, usuários e acesso** | Cadastra colaboradores, cargos, equipes e hierarquia; importa por planilha; autentica e controla o acesso por perfil | RF-001 a RF-003 (Must: RF-001, RF-003). SSO (RF-004) é Won't |
| **Competências e questionários** | Cadastra competências por cargo; cria questionários reutilizáveis; escolhe o tipo de resposta; permite questionário padrão e perguntas específicas | RF-005 a RF-010 (Must: RF-005 a RF-007) |
| **Registro de fatos e feedbacks** | Registra fatos observados e feedbacks formais e informais, positivos e construtivos, com estrutura guiada, orientações e réplica do receptor | RF-011 a RF-021 (Must: RF-011, RF-013, RF-014, RF-019, RF-021) |
| **Ciclos formais e modalidades** | Planeja ciclos com objetivos, indicadores e check-ins; suporta gestor, pares, equipe, ascendente, autoavaliação e 360°; define o modo de identificação; consolida os resultados | RF-022 a RF-036 (Must: RF-022 a RF-025, RF-027, RF-030) |
| **Sessão e notificações** | Agenda a sessão de feedback com lembrete; envia lembretes de pendências e prazos; registra check-ins periódicos | RF-037 a RF-041 |
| **Plano de ação e metas** | Cria e acompanha planos de ação a partir de feedbacks construtivos; cadastra metas individuais e de equipe | RF-042 a RF-047 (Must: RF-042, RF-043, RF-046) |
| **Histórico, painéis e análise** | Mantém o histórico de cada colaborador; oferece painéis com tendências e gráficos para o colaborador, o gestor e o RH; exporta relatórios | RF-048 a RF-052 (Must: RF-048, RF-049) |
| **Conformidade legal** | Aviso de privacidade, direitos do titular, consentimento, retenção, incidentes, canal de denúncias e acessibilidade | RF-053 a RF-065 (Must: RF-053, RF-055 a RF-060, RF-062, RF-065) |

**Qualidades do sistema.** Segurança e privacidade (RNF-001 a RNF-006), acessibilidade (RNF-017 a RNF-023), desempenho e disponibilidade (RNF-008 a RNF-011), português do Brasil (RNF-016) e parametrização sem alterar código (RNF-026).

**Regras de negócio.** Todo feedback se baseia em fatos (RN-001), não pode ser excluído, só editado com versões (RN-003), e a identidade do emissor segue o modo definido (RN-004). Demais regras estão na seção 6 da Lista Geral de Requisitos.

**Totais da lista.** São 117 requisitos: 65 funcionais, 36 não funcionais e 16 regras de negócio. Destes, 61 são Must, 44 Should, 8 Could e 4 Won't.

---

## 7. Restrições

| Restrição | O que significa para o produto | Requisitos |
|---|---|---|
| **Plataforma web** | O sistema é uma aplicação web acessada por navegador | RNF-030 |
| **LGPD** | Conformidade com a Lei nº 13.709/2018. O consentimento não é a base legal padrão. Coletar só o necessário. Dados sensíveis não são coletados. Direitos do titular atendidos pelo sistema | RNF-031, RN-012, RN-013, RF-053 a RF-063 |
| **Futuro aplicativo móvel** | A primeira versão é web responsiva. A API independente prepara o aplicativo iOS e Android, que fica para uma versão futura (Won't) | RNF-027, RNF-028, RNF-035, RNF-036 |
| **Acessibilidade** | ABNT NBR 17225:2025 e WCAG 2.2, níveis A e AA, por exigência da Lei Brasileira de Inclusão | RNF-017 a RNF-023, RF-065 |
| **Idioma** | Interface e conteúdos em português do Brasil | RNF-016 |
| **Uma organização por instalação** | Cada instalação atende uma única organização | RN-010 |
| **Serviço (SaaS) e dados no exterior** | Registros de acesso por no mínimo 6 meses; transferência internacional só com mecanismo da LGPD | RNF-032, RNF-033 |
| **Limites do produto** | Não é canal de denúncia e não decide promoção, salário ou desligamento | RN-009, RN-007 |
| **Integrações** | Sem SSO nem API de RH nesta versão; cadastro manual ou por planilha | RF-004, RNF-025, RF-002 |

---

## 8. Pontos em aberto

A Lista Geral de Requisitos (seção 9) traz dez decisões que dependem de confirmação da PO. As que mais afetam a visão do produto são:

| Ponto | Decisão adotada |
|---|---|
| P-01 Confidencial ou anônimo entre pares, equipe e na avaliação ascendente | Confidencial como padrão, anônimo como opção por ciclo |
| P-02 Quem da diretoria vê resultados | Diretoria vê só indicadores agregados |
| P-03 Mínimo de respondentes | 3, configurável |
| P-05 Prazo de guarda após o desligamento | 5 anos, configurável |
| P-10 Metas numéricas de desempenho, disponibilidade e backup | Valores propostos pela pesquisa documental |

Os demais (P-04, P-06 a P-09) tratam de edição de feedback, relatos de colegas, ocultação de respostas, problemas por cargo e check-ins periódicos. Se a PO decidir de outra forma, a mudança segue o processo de gestão de mudanças e atualiza a lista de requisitos e este documento.

---

## 9. Fontes

| Fonte | Artefato | Issue |
|---|---|---|
| Lista consolidada | [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) | #45 |
| Entrevistas (E01 e E02) | [Síntese dos Requisitos das Entrevistas](elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md) | #41 |
| Questionários (Q01 e Q02) | [Síntese dos Requisitos dos Questionários](elicitacao/questionarios/Sintese.md) | #42 |
| Pesquisa documental | [Requisitos extraídos da Pesquisa Documental](elicitacao/pesquisa-documental/Requisitos_Pesquisa_Documental.md) | #33 |
| Sistema análogo (15Five) | [Síntese dos Requisitos do Sistema Análogo](elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md) | #43 |
| Processo atual (AS-IS 1 e 2) | [Processo AS-IS de feedback e avaliação, com as dores](elicitacao/bpmn/Processo_AS-IS_e_Dores.md) | #44 |
| Enunciado | Projeto da Disciplina (área, escopo e restrições definidos pela professora) | |
