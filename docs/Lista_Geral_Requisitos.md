# Lista Geral de Requisitos

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Disciplina:** Domínios de Software (2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #45 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Verônica Ribeiro Oliveira Palmeira
**Artefatos relacionados:** [Lista_Geral_Requisitos.csv](Lista_Geral_Requisitos.csv) (mesmos requisitos, com todos os atributos, para a matriz de rastreabilidade)

**Entradas consolidadas:**

| Fonte | Artefato | Issue |
|---|---|---|
| Entrevistas (E01 e E02) | [Síntese dos Requisitos das Entrevistas](elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md) | #41 |
| Questionários (Q01 e Q02) | [Síntese dos Requisitos dos Questionários](elicitacao/questionarios/Sintese.md) | #42 |
| Pesquisa documental | [Requisitos extraídos da Pesquisa Documental](elicitacao/pesquisa-documental/Requisitos_Pesquisa_Documental.md) | #33 |
| Sistema análogo (15Five) | [Síntese dos Requisitos do Sistema Análogo](elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md) | #43 |
| Enunciado do trabalho | Projeto da Disciplina (área, escopo e restrições definidos pela professora) | — |

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Método de consolidação](#2-método-de-consolidação)
3. [Resumo](#3-resumo)
4. [Requisitos funcionais](#4-requisitos-funcionais)
5. [Requisitos não funcionais](#5-requisitos-não-funcionais)
6. [Regras de negócio](#6-regras-de-negócio)
7. [Cobertura do escopo do trabalho](#7-cobertura-do-escopo-do-trabalho)
8. [Conflitos e decisões da consolidação](#8-conflitos-e-decisões-da-consolidação)
9. [Fora do escopo](#9-fora-do-escopo)
10. [Rastreabilidade dos requisitos candidatos](#10-rastreabilidade-dos-requisitos-candidatos)
11. [Limitações](#11-limitações)

---

## 1. Objetivo

Reunir em uma única lista os requisitos levantados em todas as fontes de elicitação, sem repetições e sem conflitos em aberto, cada um com identificador definitivo, tipo, origem e prioridade.

Esta lista é a base dos artefatos seguintes: Documento Visão (#46), diagrama de casos de uso (#47), especificação suplementar (#51), modelo de dados (#52), especificação IEEE 830 (#54) e matriz de rastreabilidade (#49).

---

## 2. Método de consolidação

### 2.1 Fontes

| Fonte | Candidatos | Requisitos definitivos que a citam |
|---|---|---|
| Entrevistas (`RE`) | 37 | 51 |
| Questionários (`RQ`) | 21 | 23 |
| Pesquisa documental (`RD`) | 59 | 67 |
| Sistema análogo (`RA`) | 26 | 36 |
| Enunciado do trabalho (`ESC`) | — | 20 |
| Transcrição, sem candidato anterior | — | 1 (RF-026) |
| **Total de candidatos** | **143** | |

O processo de negócio em BPMN (#44) foi desconsiderado pelo grupo, por isso não há candidatos `RP-xx`. As dores do processo atual foram tiradas diretamente das entrevistas e dos questionários.

### 2.2 Passos

1. **Leitura das fontes.** Foram lidas as quatro sínteses, as transcrições das duas entrevistas, os dois questionários respondidos, o relatório da pesquisa documental, a descrição do 15Five e o enunciado do trabalho. As transcrições foram relidas para conferir a evidência de cada requisito e decidir os conflitos.
2. **Agrupamento por assunto.** Os candidatos que tratam da mesma necessidade foram reunidos em um único requisito. A coluna **Origem** lista todos os candidatos que deram origem a ele, como pede a seção 5.2 do [processo de requisitos](Processo_Requisitos.md).
3. **Separação.** Candidatos que misturavam mais de uma necessidade foram divididos, para que cada requisito descreva uma só necessidade e possa ser verificado (lista de verificação da seção 2.4 do processo).
4. **Classificação.** Cada requisito foi classificado como RF, RNF ou RN, conforme as definições da seção 5.2 do processo. Os RNF levam a característica da ISO/IEC 25010:2023. As restrições legais e de plataforma ficaram como RNF, na seção 5.10, porque serão tratadas na especificação suplementar (#51).
5. **Resolução de conflitos.** Quando as fontes divergiam, prevaleceu a fala da PO e, depois dela, a obrigação legal. Quando a PO não tratou do assunto, a decisão seguiu a fonte com evidência mais forte e a opção mais protetiva para o colaborador. Cada decisão, com a sua justificativa, está na seção 8.
6. **Priorização.** A prioridade proposta nas sínteses foi revista com os critérios MoSCoW do processo (seção 7), aplicados a todas as fontes ao mesmo tempo (seção 2.3).
7. **Verificação de cobertura.** Cada item do enunciado foi ligado aos requisitos que o atendem (seção 7), e cada candidato foi ligado ao requisito definitivo para onde foi (seção 10). Nenhum candidato ficou sem destino.

### 2.3 Critérios de prioridade aplicados

| Prioridade | Quando foi usada nesta lista |
|---|---|
| **Must** | Item do enunciado do trabalho; pedido da PO como essencial ou importante; obrigação legal direta (LGPD, Lei Brasileira de Inclusão); núcleo do domínio (emissor, receptor, fatos, tipo, plano de ação) |
| **Should** | Pedido da PO ou de mais de uma fonte, sem ser essencial; boa prática derivada de lei; obrigação do controlador que o sistema apenas apoia; meta numérica proposta pela pesquisa documental |
| **Could** | Citado por uma única fonte; ideia vinda só do sistema análogo; melhoria de conforto |
| **Won't** | Função da versão móvel futura; integração externa não pedida pela PO |

Requisitos citados por mais fontes subiram de prioridade, como manda o passo 2 da seção 7 do processo. Toda mudança em relação à prioridade proposta na síntese de origem está explicada na coluna **Observações**.

### 2.4 Como ler as tabelas

| Coluna | Conteúdo |
|---|---|
| **ID** | Identificador definitivo. `RF-001` funcional, `RNF-001` não funcional, `RN-001` regra de negócio. Os números não serão reutilizados |
| **Origem** | Candidatos que deram origem ao requisito: `RE` entrevista, `RQ` questionário, `RD` pesquisa documental, `RA` sistema análogo. `ESC` indica o enunciado do trabalho. `E01 §n` indica um trecho da transcrição usado diretamente |
| **Prioridade** | Must, Should, Could ou Won't (seção 2.3) |
| **Observações** | Evidência principal e decisões tomadas na consolidação (seção 8) |

**Atributos comuns a todos os requisitos.** Nesta versão, todos estão com status **Aprovado** (sintetizados, classificados, priorizados e aceitos na consolidação, conforme o ciclo de vida da seção 6.2 do processo), inclusive os Won't, que ficam registrados para a versão futura. A responsável pela especificação é a autora deste documento. Os dois atributos estão no [CSV](Lista_Geral_Requisitos.csv), linha a linha.

**Códigos das fontes nas observações.** E01 = entrevista com a PO (Profa. Adriana); E02 = entrevista com a Secretária Municipal de Educação; Q01 e Q02 = questionários; § = seção da transcrição ou do questionário.

**Termos usados.** As definições abaixo valem para esta lista. O glossário completo será feito na issue #53.

| Termo | Significado nesta lista |
|---|---|
| Emissor | Quem dá o feedback ou responde a uma avaliação |
| Receptor | Quem recebe o feedback; pode ser um colaborador ou uma equipe |
| Fato | Comportamento ou resultado observado, com data, que fundamenta um feedback |
| Feedback formal | Feedback planejado dentro de um ciclo, com objetivos, indicadores e check-ins |
| Feedback informal | Feedback dado a qualquer momento, sem planejamento (*ad hoc*) |
| Ciclo | Período planejado de feedback formal, com participantes, modalidades e datas |
| Check-in | Ponto de verificação dentro de um ciclo ou de um plano de ação |
| Modalidade | Quem avalia quem: gestor → colaborador, ascendente, pares, equipe, autoavaliação ou 360° |
| Identificado, confidencial, anônimo | Modos de identificação do emissor, definidos em RN-004 |

---

## 3. Resumo

| Tipo | Must | Should | Could | Won't | Total |
|---|---|---|---|---|---|
| RF | 30 | 26 | 8 | 1 | 65 |
| RNF | 18 | 14 | 1 | 3 | 36 |
| RN | 13 | 3 | 0 | 0 | 16 |
| **Total** | **61** | **43** | **9** | **4** | **117** |

Dos 61 requisitos Must, 24 vêm só da pesquisa documental (obrigações da LGPD e da Lei Brasileira de Inclusão, normas de acessibilidade) ou das restrições do enunciado. Os outros 37 atendem a pedidos da PO, a itens do enunciado e ao núcleo do domínio. A proporção de Must (52% da lista) é coerente com o pedido da PO de requisitos amplos: o escopo pode ser reduzido na arquitetura, por exemplo só a gestor e colaborador (E01 §24), sem reduzir os requisitos.

| Fontes diferentes que confirmam o requisito | Quantidade |
|---|---|
| Três ou mais | 21 |
| Duas | 29 |
| Uma | 67 |

---

## 4. Requisitos funcionais

### 4.1 Organização, usuários e acesso

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-001 | O sistema deve permitir que o RH ou o administrador cadastre colaboradores, cargos, equipes e a hierarquia da organização (quem é gestor de quem), com quantos níveis hierárquicos forem necessários. | RE-28 | Must | Hierarquia em níveis, como professor → diretor → secretária (E02 §1). A hierarquia define o gestor direto usado em RNF-001. |
| RF-002 | O sistema deve permitir importar colaboradores, cargos, equipes e hierarquia a partir de planilha (CSV), como alternativa ao cadastro manual. | RE-28; RD-39 | Should | A PO aceita o cadastro manual quando não houver importação (E01 §30), por isso não é Must. |
| RF-003 | O sistema deve autenticar cada usuário e liberar as funções de acordo com o seu perfil: colaborador, gestor, RH ou administrador. Um mesmo usuário pode acumular perfis, como o gestor que também é avaliado pelo seu superior. | RE-27; RD-14 | Must | O acúmulo de perfis decorre da hierarquia em vários níveis (E02 §1) e da avaliação ascendente (RF-024). |
| RF-004 | O sistema deve permitir login único (SSO) com o provedor de identidade da organização. | RA-23 | Won't | Integração externa não pedida pela PO (critério Won't do processo, seção 7). |

### 4.2 Competências e questionários

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-005 | O RH ou o administrador deve poder cadastrar competências e associá-las aos cargos, formando o conjunto de competências fixas de cada cargo. | RE-11; RA-17; RQ-02 | Must | Competências fixas por cargo (E01 §9). |
| RF-006 | O gestor deve poder atribuir a um colaborador ou a um grupo competências específicas, além das competências fixas do cargo. | RE-11; RA-17; ESC | Must | "Quem tem geralmente o maior poder é o gestor" (E01 §10). O enunciado pede orientar o receptor sobre suas "competências específicas". |
| RF-007 | O sistema deve permitir criar questionários de avaliação, com perguntas vinculadas às competências e aos cargos, e salvá-los como modelos reutilizáveis em outros ciclos. | RE-12; RA-14; RQ-02; ESC | Must | Uso de questionário é item do enunciado. Recurso com a maior utilidade média nos questionários (4,0 de 4). |
| RF-008 | O RH deve poder definir um questionário padrão da organização, e o gestor deve poder acrescentar a ele perguntas específicas para um colaborador. | RE-12 | Should | "Formulário pré-pronto de avaliação do RH", com outras metas para alguns indivíduos (E01 §29). |
| RF-009 | Para cada pergunta ou indicador, o sistema deve permitir escolher o tipo de resposta: escala ordinal, valor numérico, atingido/não atingido ou texto livre. | RE-13 | Should | Subiu de Could para Should: sem respostas em escala não há os números que a análise com tendências e gráficos do enunciado exige. Escala "ordinal" ou "numérica" (E01 §27). |
| RF-010 | O sistema deve permitir atribuir pesos diferentes aos feedbacks de um período e aos indicadores de um mesmo feedback no cálculo dos resultados consolidados. | RE-14 | Could | Fonte única (E01 §37). O cálculo deve exibir os critérios usados (RN-008). |

### 4.3 Registro de fatos e de feedbacks

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-011 | O emissor deve poder registrar fatos e comportamentos observados de um colaborador ao longo do período, com data e descrição, e vinculá-los depois a um ou mais feedbacks. Até o vínculo, o fato registrado é visível apenas para quem o registrou. | RE-02; RA-02 | Must | "Eu coleto fatos, registro os fatos, e depois eu posso linkar" (E01 §1). Resolve o ponto 1 da síntese do sistema análogo: o registro prévio é uma função própria, não só um campo do feedback. |
| RF-012 | O gestor deve poder registrar como fato um relato recebido de outro colaborador, marcado como "relato", sem que o receptor do feedback veja quem relatou. O relato só pode embasar um feedback depois de confirmado pela observação do próprio gestor. | RE-05 | Could | A confirmação pelo gestor mantém RN-001; é o que a E02 já faz: "eu sempre procuro ver por mim mesma antes de falar com a pessoa" (E02 §4). Fonte única (E02 §3). |
| RF-013 | O sistema deve permitir registrar um feedback com emissor, receptor (colaborador ou equipe), data, tipo (positivo ou construtivo), modalidade (formal ou informal), descrição e os fatos que o motivaram. | RE-01; RA-24; ESC | Must | Núcleo do domínio (processo, seção 7). Campos obrigatórios em RN-002. |
| RF-014 | O sistema deve permitir registrar um feedback informal a qualquer momento, sem ciclo ou planejamento prévio, inclusive para um colaborador de outra área. | RE-04; RA-03; ESC | Must | O informal é ad hoc, "sob demanda" (E01 §12). Feedback para pessoa de outra área (E01 §10). |
| RF-015 | O sistema deve oferecer um formulário simplificado para o feedback positivo informal (reconhecimento), que peça apenas os campos obrigatórios de RN-002. | RE-04; RA-03 | Should | O positivo é o feedback menos frequente (E01 §20; E02 §2) e hoje é dado por WhatsApp (E02 §2). Resolve o ponto 5 da síntese do sistema análogo: o fato continua obrigatório, mas o formulário é curto. |
| RF-016 | Ao escolher o tipo do feedback, o sistema deve apresentar a estrutura correspondente. Positivo: ação ou comportamento, resultados e repercussão para o gestor, o time e a organização. Construtivo: aspecto positivo, fatos, problema, repercussão, reflexão e plano de ação. | RE-03; RA-21 | Should | "A pessoa escolhe essa categoria e já vem uma estrutura": "seria interessante" (E01 §16). |
| RF-017 | O sistema deve oferecer orientações sobre como dar e como receber feedback, com exemplos de feedback positivo e construtivo, disponíveis durante o registro. | RE-23; RQ-03; RD-37; RA-21 | Should | Subiu de Could para Should por aparecer em quatro fontes. "Gestores não sabem dar feedback" foi o problema citado nos dois questionários. |
| RF-018 | Nos campos de texto livre, o sistema deve orientar o emissor a descrever fatos e comportamentos observáveis e a não incluir dados sensíveis, informações de saúde ou dados de terceiros. | RD-06 | Should | Boa prática derivada da LGPD (arts. 6º, III, e 11). |
| RF-019 | Antes do envio de um feedback ou de uma avaliação, o sistema deve informar ao emissor, em linguagem clara, quem poderá ver o conteúdo e a sua identidade, conforme o modo de identificação (RN-004). | RD-16; RA-05 | Must | Transparência (LGPD, art. 6º, VI). O rótulo "anônimo" só pode ser usado no modo anônimo de RN-004. |
| RF-020 | O receptor deve poder registrar uma manifestação (réplica) sobre um feedback recebido, sem alterar o conteúdo escrito pelo emissor. | RD-09 | Should | Boa prática derivada da LGPD (arts. 6º, V, e 18, III). |
| RF-021 | O sistema deve permitir vincular cada feedback a uma ou mais competências do receptor. | RA-04; RE-11 | Must | Necessário para a evolução por competência (RF-049) e para orientar o receptor sobre suas competências (enunciado). |

### 4.4 Ciclos formais e modalidades de feedback

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-022 | O gestor ou o RH deve poder planejar um ciclo de feedback formal, informando período, receptor (indivíduo ou equipe), objetivos de comportamento ou de resultado, competências, questionário, modalidades, participantes e datas dos check-ins. | RE-06; RA-09; RQ-01; ESC | Must | Periodicidade configurável, por exemplo de 3 ou 4 meses (E01 §5), e não só anual (Q01 §3). A PO descreve o gestor como quem planeja (E01 §5, §17); o RA-09 atribuía o ciclo só ao administrador. |
| RF-023 | Para cada objetivo de um ciclo formal, o sistema deve permitir definir indicadores, com a fonte de evidência e o valor esperado, e registrar o valor observado em cada check-in. | RE-07; RA-16 | Must | Subiu de Should para Must: ao planejar os check-ins e os indicadores, a PO destacou "aqui é importante" (E01 §5) e os apontou como a forma de reduzir a subjetividade (E01 §29). Fontes de evidência citadas: avaliação do cliente, do setor parceiro, pontualidade das entregas (E01 §5, §14). |
| RF-024 | O sistema deve suportar as modalidades gestor → colaborador, colaborador → gestor (ascendente), entre pares, de equipe (todos avaliam todos), autoavaliação e 360°, e permitir combinar várias delas em um mesmo ciclo. | RE-18; RA-10; RQ-15; ESC | Must | Modalidades confirmadas pela PO (E01 §12) e exigidas no enunciado. A PO admite restringir a arquitetura a gestor e colaborador (E01 §24); isso não altera o requisito. |
| RF-025 | Na avaliação 360°, o gestor deve abrir o ciclo e selecionar ou convidar os participantes, que precisam ser membros do seu time. | RE-19; RA-11 | Must | Segue a PO (E01 §14, §21). O RA-11, em que o avaliado indicava os pares, foi corrigido conforme o ponto 9 da síntese das entrevistas. |
| RF-026 | Ao abrir um ciclo formal, o sistema deve notificar cada avaliado sobre os objetivos, as competências e os indicadores pelos quais será avaliado e sobre as datas dos check-ins. | E01 §29; E01 §19 | Should | Identificado na consolidação, sem candidato anterior: "é isso que eu vou estar avaliando e as pessoas vão ser notificadas sobre isso" (E01 §29); com feedback estabelecido, as pessoas "sabem o que que é esperado delas" (E01 §19). |
| RF-027 | Cada participante convidado deve poder responder, dentro do prazo do ciclo, ao questionário da modalidade em que avalia. | RE-18; RE-19; RA-10; ESC | Must | Função básica para que o questionário apoie a avaliação feita pelos emissores (enunciado). |
| RF-028 | Ao responder uma avaliação formal, o avaliador deve poder consultar os fatos e os feedbacks registrados sobre o avaliado no período do ciclo, respeitadas as regras de visibilidade. | RA-15; ESC | Should | Avaliação "baseada sempre em dados coletados dos emissores" (enunciado); reaproveitamento das informações (E01 §15). |
| RF-029 | O sistema deve registrar quem foi convidado para uma avaliação e não respondeu no prazo, e mostrar essa informação ao gestor e ao RH, sem aplicar nenhuma consequência automática. | RE-20 | Should | "A informação que eu tenho que saber é: tal pessoa não participou"; consequências estão fora do escopo (E01 §21). |
| RF-030 | O RH ou o administrador deve poder configurar, por ciclo e por modalidade, o modo de identificação do emissor, dentro do que RN-004 permite. | RA-12; RD-15; RE-33 | Must | Entre pares e na equipe, "a gente pode parametrizar isso" (E01 §11). |
| RF-031 | O colaborador deve poder solicitar feedback a um ou mais colegas a qualquer momento, fora do ciclo formal, informando o tema e o prazo de resposta. | RQ-06; RA-06 | Should | Avaliado como "útil" nos dois questionários. |
| RF-032 | Ao encerrar um ciclo, o sistema deve consolidar automaticamente os resultados de cada avaliado por competência, por indicador e por modalidade. | RQ-16 | Should | Hoje a consolidação de um ciclo leva cerca de 1 semana (Q02). Ganho claro para gestor e RH (critério Should). |
| RF-033 | O sistema deve comparar a autoavaliação de um colaborador com a avaliação feita pelos demais avaliadores do ciclo, mostrando onde as percepções convergem ou divergem. | RE-21; RQ-18 | Should | "A minha percepção sobre a percepção dos meus colegas sobre mim" (E01 §14). |
| RF-034 | Após a sessão de feedback, o sistema deve permitir que o emissor avalie a postura do receptor (colaborativa ou reativa) e que o receptor avalie se o feedback agregou valor. | RE-22 | Should | Serve "para a gente poder verificar se o processo de feedback está rodando" (E01 §13). |
| RF-035 | Antes da liberação dos resultados de um ciclo, o RH deve poder ocultar do avaliado uma resposta inadequada, sem apagá-la, com registro na trilha de auditoria e aviso ao emissor. | RA-13 | Could | Ideia vinda do sistema análogo. Ocultar não é excluir, o que preserva RN-003. |
| RF-036 | O sistema deve permitir alternar as perguntas dos check-ins periódicos entre um período e outro. | RA-26 | Could | Ideia vinda só do sistema análogo (usuários do 15Five repetem as respostas). Reclassificado de RN para RF, porque descreve uma função do sistema. |

### 4.5 Sessão de feedback e notificações

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-037 | O emissor deve poder agendar a sessão de feedback com data, hora, participantes e assunto, e o sistema deve enviar aos participantes um comunicado da sessão e um lembrete antes dela. | RE-08; RA-08 | Should | A falta de horário é a maior dificuldade da E02 (E02 §2). A PO pede "comunicado de sessão" e "lembrete" (E01 §5). |
| RF-038 | Ao agendar uma sessão, o sistema deve sugerir horários em que emissor e receptor estejam livres. | RE-09 | Could | Única coisa pedida ao sistema pela E02 (E02 §8), mas fonte única e dependente de o sistema conhecer a agenda dos usuários. O essencial é atendido pelo agendamento com lembrete (RF-037). |
| RF-039 | A sessão agendada deve ter uma pauta compartilhada entre os participantes, e cada participante deve poder fazer anotações privadas, visíveis só para ele. | RA-08 | Could | Ideia vinda só do sistema análogo (critério Could). |
| RF-040 | O sistema deve enviar lembretes de avaliações pendentes, de check-ins e de prazos de planos de ação, e cada usuário deve poder desativá-los. | RQ-21 | Could | "Pouco útil" (Q01) e "útil" (Q02), média 2,5. O lembrete da sessão de feedback está em RF-037. |
| RF-041 | O sistema deve permitir registrar check-ins periódicos entre gestor e colaborador, com frequência configurável, vinculados às metas e aos planos de ação em andamento. O gestor define para quais colaboradores da sua equipe os check-ins periódicos valem. | RA-01; RE-06 | Should | O gestor decide a quem se aplicam, seguindo a PO: "eu prefiro assim não ser restritiva", e o gestor "verifica o que que ele acha que é melhor" (E01 §21). Os check-ins do ciclo formal estão em RF-022 e RF-023. |

### 4.6 Plano de ação e metas de desenvolvimento

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-042 | A partir de um feedback construtivo, o sistema deve permitir criar um plano de ação com ações, responsáveis, metas, pontos de monitoramento e data final. | RE-15; RA-18; RQ-07; ESC | Must | Plano construído em conjunto (RN-006). Recurso com utilidade média 4,0 nos questionários. Plano de ação de melhoria é item do enunciado. |
| RF-043 | O sistema deve permitir acompanhar o plano de ação: registrar o resultado de cada ponto de monitoramento, ajustar as ações e, na data final, registrar se houve melhora ou se é necessário um novo feedback. | RE-16; RA-18; ESC | Must | Sem esse registro "eu não tenho controle se houve uma melhora" (E01 §6). |
| RF-044 | O gestor deve poder acompanhar o andamento dos planos de ação da sua equipe, e o RH, os de toda a organização. | RQ-17; RE-25 | Should | "Planos de ação em andamento" é o que a gestora do Q02 mais precisa acompanhar; "o RH tem que ter esse controle" (E01 §10). |
| RF-045 | O sistema deve permitir consultar quais feedbacks e planos de ação resultaram em melhora do colaborador. | RE-17 | Should | "Quais são os feedbacks que tiveram um bom desempenho" (E01 §4). |
| RF-046 | O colaborador e o gestor devem poder cadastrar metas de desenvolvimento individuais, com descrição, competência relacionada, indicador, valor esperado e prazo, e atualizar o progresso ao longo do tempo. | RA-16; RQ-08; ESC | Must | Planejamento de desenvolvimento com metas é item do enunciado. Definição conjunta em RN-006. |
| RF-047 | O gestor e a equipe devem poder cadastrar metas da equipe para um período, como um bimestre, e registrar se foram atingidas. | RE-10 | Should | Metas bimestrais definidas com autonomia das equipes (E02 §7). |

### 4.7 Histórico, painéis e análise

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-048 | O sistema deve manter o histórico de cada colaborador, com os feedbacks recebidos, as avaliações, os planos de ação e as metas, em ordem cronológica. | RE-24; RQ-09; RD-47; ESC | Must | "Guarda histórico dos feedbacks" (enunciado). Hoje não existe histórico (E02 §7). |
| RF-049 | O sistema deve oferecer ao colaborador um painel com a evolução de cada indicador e de cada competência ao longo do tempo, em gráficos; seus pontos fortes e pontos a melhorar; o andamento de suas metas e planos de ação; e os comentários recebidos. | RE-24; RQ-10; RQ-19; RA-20; ESC | Must | Análise com tendências, números e recursos visuais (enunciado). Todo gráfico atende a RNF-007 e RNF-020. |
| RF-050 | O sistema deve oferecer ao gestor, para a sua equipe, e ao RH, para a organização, um painel com indicadores consolidados, tendências ao longo do tempo e a situação dos planos de ação e das metas. | RE-25; RQ-16; RQ-17; RA-20; ESC | Should | Dados de fontes confidenciais ou anônimas obedecem a RN-005. |
| RF-051 | O RH deve poder exportar o histórico de um colaborador em relatório. | RD-47 | Should | O histórico resguarda a organização juridicamente (E01 §32). |
| RF-052 | O sistema deve permitir consultar os problemas recorrentes associados a um cargo, mesmo depois que o ocupante saiu, apenas de forma agregada e sem identificar os ocupantes anteriores. | RE-26 | Could | Fonte única. "Às vezes os problemas estão relacionados ao cargo em si, não à pessoa" (E02 §6). |

### 4.8 Conformidade legal: LGPD e acessibilidade

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-053 | O sistema deve disponibilizar, em local fixo e acessível de qualquer tela, o aviso de privacidade com finalidades, bases legais, compartilhamentos, prazos de retenção, direitos do titular e identidade e contato do encarregado. | RD-01 | Must | LGPD, arts. 6º, VI, 9º e 41, §1º. |
| RF-054 | O sistema deve permitir que o administrador cadastre a finalidade e a base legal de cada categoria de dado tratado e exporte esse inventário, para apoiar o registro das operações e o relatório de impacto (RIPD). | RD-02 | Should | Dever do controlador que o sistema apoia (LGPD, arts. 37 e 38). |
| RF-055 | Quando houver funcionalidade opcional baseada em consentimento, o sistema deve registrar quem consentiu, quando, para qual finalidade e em qual versão do termo, e permitir a revogação a qualquer momento por meio tão simples quanto o usado para consentir. | RD-04; RQ-12 | Must | O RQ-12 foi ajustado: o consentimento não é a base legal do tratamento principal (RN-012). |
| RF-056 | O colaborador deve poder confirmar a existência de tratamento e acessar seus dados pessoais pelo próprio sistema, de forma imediata e simplificada ou por declaração completa (origem, critérios e finalidade) em até 15 dias, sem revelar a identidade de emissores confidenciais. | RD-07 | Must | LGPD, arts. 18, I e II, e 19. O direito de acesso do avaliado não anula a proteção do emissor confidencial (pesquisa documental, seção 8). |
| RF-057 | O colaborador deve poder solicitar a correção de dados cadastrais incompletos, inexatos ou desatualizados. | RD-08 | Must | LGPD, art. 18, III. |
| RF-058 | O colaborador deve poder exportar seus dados (cadastro, feedbacks recebidos, metas e planos de ação) em formato estruturado e legível por máquina, como JSON ou CSV. | RD-10 | Must | LGPD, art. 18, V. A regulamentação da ANPD sobre o tema ainda está pendente (FD-08). |
| RF-059 | O colaborador deve poder solicitar a anonimização, o bloqueio ou a eliminação de dados desnecessários ou excessivos e a eliminação dos dados tratados com base em consentimento, ressalvadas as hipóteses de conservação do art. 16 da LGPD. | RD-11 | Must | LGPD, arts. 16 e 18, IV e VI. |
| RF-060 | O sistema deve informar ao colaborador com quais entidades públicas e privadas seus dados foram compartilhados. | RD-12 | Must | LGPD, art. 18, VII. |
| RF-061 | O sistema deve oferecer ao RH e ao encarregado de dados da organização uma fila de solicitações de titulares, com data de abertura, prazo, status, responsável, histórico e resposta enviada. | RD-13 | Should | Dever do controlador que o sistema apoia (LGPD, arts. 18 e 19). |
| RF-062 | O sistema deve permitir configurar a política de retenção por categoria de dado (feedbacks, planos de ação, registros de acesso), com eliminação ou anonimização automática ao fim do prazo, inclusive após o desligamento, e com bloqueio da eliminação quando houver processo judicial em curso. | RD-24; RE-36 | Must | LGPD, arts. 15 e 16. O prazo padrão está em RN-011. |
| RF-063 | O sistema deve apoiar a gestão de incidentes de segurança: alertar eventos suspeitos, registrar o incidente (data, dados e titulares afetados, medidas adotadas), gerar a lista de titulares a comunicar e guardar o registro por no mínimo 5 anos. | RD-26 | Should | Dever do controlador que o sistema apoia: comunicar a ANPD e os titulares em até 3 dias úteis (LGPD, art. 48; Res. CD/ANPD nº 15/2024). |
| RF-064 | O sistema deve exibir um atalho visível para o canal de denúncias da organização e orientar o usuário a usá-lo quando o relato for de assédio ou de conduta grave. | RD-48; RE-35 | Should | Lei nº 14.457/2022, art. 23, para organizações obrigadas a ter CIPA. Complementa RN-009. |
| RF-065 | O sistema deve exibir o símbolo de acessibilidade em destaque e uma página de declaração de acessibilidade com o nível de conformidade e um canal para reportar barreiras. | RD-58 | Must | Lei Brasileira de Inclusão, art. 63, §1º. |

---

## 5. Requisitos não funcionais

### 5.1 Segurança

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-001 | Um feedback e o resultado de avaliação de um colaborador só podem ser vistos pelo próprio colaborador, pelo emissor (apenas o conteúdo que ele escreveu), pelo gestor direto do colaborador e pelo RH. A diretoria da organização vê apenas indicadores agregados, conforme RN-005. | Segurança (confidencialidade) | RE-29; RQ-05; RD-14 | Must | Une a E01 (receptor, emissor e RH, §11) e os questionários (pessoa, gestor direto e RH). Só o Q02 incluiu a Diretoria; por isso ela vê apenas dados agregados (necessidade, LGPD, art. 6º, III). |
| RNF-002 | Todo feedback novo deve ficar visível apenas ao público mínimo de RNF-001. A visibilidade é definida no envio e só pode ser ampliada por nova ação explícita do emissor. | Segurança (confidencialidade) | RD-22; RA-07 | Must | Privacidade por padrão (LGPD, arts. 46, §2º, e 49). O RA-07 foi unido a este requisito. |
| RNF-003 | Nos feedbacks e avaliações em modo confidencial, o vínculo entre emissor e resposta deve ser armazenado separado do conteúdo (pseudonimização), com acesso restrito ao RH e registrado na trilha de auditoria. | Segurança (confidencialidade, responsabilização) | RD-18 | Should | Boa prática derivada da LGPD (art. 13, §4º). |
| RNF-004 | Dados pessoais e conteúdo de feedback devem ser criptografados em trânsito (TLS 1.2 ou superior) e em repouso. | Segurança (confidencialidade, integridade) | RD-19 | Must | Medida técnica de segurança (LGPD, art. 46). |
| RNF-005 | O sistema deve manter trilha de auditoria inalterável dos acessos e das alterações a dados pessoais e feedbacks (quem, quando, o quê e de onde), incluindo toda consulta à identidade de emissores confidenciais. | Segurança (responsabilização, não repúdio) | RD-20 | Must | LGPD, arts. 6º, X, 37 e 46. |
| RNF-006 | O sistema deve exigir autenticação em dois fatores para RH e administradores, bloquear o acesso após tentativas sucessivas de login sem sucesso e encerrar a sessão após um período de inatividade. | Segurança (autenticidade, resistência) | RD-21 | Should | Boa prática derivada da LGPD (art. 46). Número de tentativas e tempo de inatividade a definir na especificação suplementar (#51). |

### 5.2 Adequação funcional

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-007 | Toda média, tendência ou gráfico exibido deve informar o período e o número de respostas que o compõem. | Adequação funcional (correção); Capacidade de interação (autodescritividade) | RD-43 | Should | Evita conclusões sobre poucos dados (LGPD, art. 6º, V). |

### 5.3 Eficiência de desempenho

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-008 | As telas principais (painel, formulário de feedback e histórico) devem carregar em até 3 s e o envio de um feedback deve ser confirmado em até 2 s, no percentil 95, em conexão 4G. | Eficiência de desempenho (comportamento temporal) | RD-31 | Should | Meta proposta pela pesquisa documental; detalhada na especificação suplementar (#51). |
| RNF-009 | O sistema deve suportar o pico de um ciclo formal, quando a maior parte dos colaboradores responde na mesma semana, sem descumprir RNF-008. | Eficiência de desempenho (capacidade) | RD-32 | Should | O volume de usuários será dimensionado na especificação suplementar (#51). |

### 5.4 Confiabilidade

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-010 | O sistema deve ter disponibilidade mínima de 99,5% ao mês, com janelas de manutenção comunicadas com antecedência e fora dos prazos dos ciclos de avaliação. | Confiabilidade (disponibilidade) | RD-33 | Should | Meta proposta pela pesquisa documental. |
| RNF-011 | O sistema deve ter backups criptografados diários, com perda máxima de 24 h de dados (RPO), restauração em até 4 h (RTO) e testes periódicos de restauração. | Confiabilidade (recuperabilidade) | RD-34 | Should | Meta proposta pela pesquisa documental. |
| RNF-012 | Respostas a feedbacks e questionários devem ser salvas automaticamente como rascunho, para que nada se perca em caso de queda de conexão, sessão expirada ou campos obrigatórios ainda em branco. | Confiabilidade (tolerância a falhas); Capacidade de interação (proteção contra erro do usuário) | RD-35 | Should | A PO relatou um sistema que descartava o cadastro incompleto (E01 §33). |

### 5.5 Capacidade de interação

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-013 | O registro de um feedback informal deve caber em uma única tela, com apenas os campos obrigatórios de RN-002. | Capacidade de interação (operabilidade) | RE-30 | Should | Ficar "horas preenchendo informações" atrapalharia (E02 §8); dar feedback "dá trabalho" (E01 §9). A meta "uma única tela" foi definida na consolidação para tornar o RE-30 verificável. |
| RNF-014 | Um avaliador deve conseguir concluir a avaliação de um colega em até 20 minutos. | Capacidade de interação (operabilidade) | RQ-11 | Should | 10 a 20 minutos (Q01) e mais de 20 minutos (Q02): o limite de 20 minutos atende às duas respostas. |
| RNF-015 | Os formulários devem validar os campos com mensagens claras e pedir confirmação antes de ações irreversíveis, como enviar um feedback ou encerrar um ciclo. | Capacidade de interação (proteção contra erro do usuário) | RD-36 | Should | Cuidado reforçado porque o feedback enviado não pode ser excluído (RN-003). |
| RNF-016 | A interface, as mensagens, as orientações e os modelos de perguntas devem estar em português do Brasil. | Capacidade de interação (aprendizagem) | RA-25; RD-57 | Must | Falha do 15Five, que não tem português. Os usuários do sistema são brasileiros e a LGPD exige informação clara ao titular. |
| RNF-017 | A interface web deve atender aos requisitos da ABNT NBR 17225:2025 e aos critérios de nível A e AA das WCAG 2.2. | Capacidade de interação (inclusividade) | RD-50 | Must | Obrigação legal (Lei Brasileira de Inclusão, art. 63). Os requisitos seguintes detalham os critérios mais relevantes. |
| RNF-018 | Todas as funcionalidades devem ser operáveis por teclado, com foco sempre visível e não encoberto por outros elementos. | Capacidade de interação (inclusividade, operabilidade) | RD-51 | Must | Detalha RNF-017 (WCAG 2.1.1, 2.4.7 e 2.4.11). |
| RNF-019 | O contraste deve ser de no mínimo 4,5:1 para texto normal e 3:1 para texto grande e componentes de interface, e a cor não pode ser o único meio de transmitir informação. | Capacidade de interação (inclusividade) | RD-52 | Must | Detalha RNF-017 (WCAG 1.4.1, 1.4.3 e 1.4.11). Vale para status de metas e linhas de gráficos. |
| RNF-020 | Os gráficos de evolução e de indicadores devem ter alternativa textual equivalente, com resumo e tabela de dados. | Capacidade de interação (inclusividade) | RD-53 | Must | Detalha RNF-017 (WCAG 1.1.1). |
| RNF-021 | Os formulários devem ter rótulos e instruções, identificar o erro e sugerir a correção, e não pedir de novo informação já fornecida no mesmo processo. | Capacidade de interação (inclusividade, proteção contra erro do usuário) | RD-54 | Must | Detalha RNF-017 (WCAG 3.3.1, 3.3.2, 3.3.3 e 3.3.7). |
| RNF-022 | O login não pode depender de teste cognitivo sem alternativa e deve permitir colar a senha e usar gerenciadores de senha. | Capacidade de interação (inclusividade); Segurança (autenticidade) | RD-55 | Must | Detalha RNF-017 (WCAG 3.3.8). |
| RNF-023 | As páginas devem usar HTML semântico (títulos, regiões e rótulos), declarar o idioma pt-BR, aceitar texto ampliado em 200% sem perda de conteúdo e funcionar com leitores de tela. | Capacidade de interação (inclusividade) | RD-57 | Must | Detalha RNF-017 (WCAG 1.3.1, 1.4.4, 3.1.1 e 4.1.2). |

### 5.6 Proteção

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-024 | Antes do envio, o sistema deve sinalizar ao emissor termos potencialmente ofensivos ou discriminatórios e sugerir a revisão, sem bloquear o envio. | Proteção (alerta de perigo) | RD-38 | Could | Fonte única. Relaciona-se ao feedback dado com "uma dose de agressividade" citado pela PO (E01 §20). |

### 5.7 Compatibilidade

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-025 | O sistema deve oferecer integração com sistemas de RH e de folha de pagamento por API documentada. | Compatibilidade (interoperabilidade) | RD-39 | Won't | A PO aceitou a importação por planilha ou o cadastro manual (E01 §30). A importação está em RF-002. |

### 5.8 Manutenibilidade

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-026 | Competências, questionários, modalidades de feedback e ciclos devem ser parametrizáveis pelo administrador, sem alteração de código. | Manutenibilidade (modificabilidade); Flexibilidade (adaptabilidade) | RD-40 | Should | A PO quer poder mudar perguntas e parâmetros (E01 §15, §29). |

### 5.9 Flexibilidade

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-027 | A interface deve ser responsiva: sem rolagem horizontal a 320 px de largura, funcional em retrato e paisagem e com alvos de toque de no mínimo 24 × 24 px CSS. | Flexibilidade (adaptabilidade); Capacidade de interação (operabilidade) | RD-56; RQ-20; ESC | Must | Atende desde a primeira versão à perspectiva móvel do enunciado. Divergência entre Q01 ("nada útil") e Q02 ("muito útil"). |
| RNF-028 | O back-end deve expor todas as funcionalidades por uma API independente da interface web, para que o futuro aplicativo móvel reutilize as mesmas regras de negócio. | Flexibilidade (adaptabilidade); Manutenibilidade (modularidade, reusabilidade) | RD-41; ESC | Must | Necessária desde a primeira versão para viabilizar a versão móvel futura (enunciado). |
| RNF-029 | A arquitetura deve permitir aumentar o número de colaboradores atendidos sem reescrever o sistema. | Flexibilidade (escalabilidade) | RD-42 | Should | Ajustado: o RD-42 citava também o número de organizações, mas cada instalação atende uma única organização (RN-010). |

### 5.10 Restrições

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-030 | O sistema deve ser uma aplicação web, acessada por navegador. | Restrição de plataforma | ESC | Must | Restrição do enunciado, confirmada pela PO (E01 §24). |
| RNF-031 | O sistema deve estar em conformidade com a Lei nº 13.709/2018 (LGPD). | Restrição legal | ESC | Must | Restrição do enunciado, detalhada nos requisitos de LGPD desta lista (ver seção 7). |
| RNF-032 | Se o sistema for operado como serviço (SaaS) pelo fornecedor, os registros de acesso à aplicação devem ser guardados por no mínimo 6 meses, em ambiente controlado e seguro. | Restrição legal; Segurança (responsabilização) | RD-25 | Must | Condicional: só se aplica se o sistema for oferecido como serviço (Marco Civil da Internet, art. 15). A PO admite o sistema como "um serviço que é fornecido para uma empresa" (E01 §31). |
| RNF-033 | Se os dados forem hospedados ou processados fora do Brasil, a transferência internacional deve se apoiar em um mecanismo do art. 33 da LGPD, como as cláusulas-padrão contratuais aprovadas pela ANPD. | Restrição legal | RD-28 | Must | Condicional: só se aplica a hospedagem fora do país. |
| RNF-034 | O fornecedor deve entregar documentação técnica de segurança e de fluxo de dados que permita à organização elaborar o RIPD e responder a fiscalizações. | Restrição legal | RD-30 | Should | Dever do controlador que o fornecedor apoia (LGPD, arts. 38, 39 e 50). |
| RNF-035 | Quando existir o aplicativo móvel, ele deve oferecer as mesmas funções em iOS e Android, a partir da mesma API da versão web. | Restrição de plataforma | RA-22 | Won't | Função da versão móvel futura (critério Won't). A base para ela está em RNF-028. |
| RNF-036 | O futuro aplicativo móvel deve atender à ABNT NBR 17060:2022 (acessibilidade em aplicativos de dispositivos móveis). | Restrição legal; Capacidade de interação (inclusividade) | RD-59 | Won't | Função da versão móvel futura (critério Won't). |

---

## 6. Regras de negócio

| ID | Regra | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RN-001 | Todo feedback deve se basear em fatos ou comportamentos observados. Não pode tratar de traços de personalidade, opiniões ou aspectos da vida privada, e os questionários não podem pedir esse tipo de avaliação. | RE-31; RD-44; RA-24; ESC | Must | Fatos são campo obrigatório "porque você não entra muito no nível de subjetividade" (E01 §2); "minha opinião não vale" (E01 §20). |
| RN-002 | São obrigatórios em todo feedback: emissor, receptor, data, tipo, modalidade e pelo menos um fato. | RA-24; RE-01 | Must | Vale também para o feedback positivo, que a PO exemplifica com fatos (E01 §1). |
| RN-003 | Um feedback registrado não pode ser excluído, porque é registro oficial do histórico do colaborador. O emissor pode editá-lo, e cada alteração gera uma nova versão datada, sem apagar a anterior. | RE-32; RD-47 | Must | "Deletar não dá... aquilo ali é uma informação oficial" (E01 §20). A PO vetou só a exclusão; a edição com versões (RD-47) corrige erros sem perder o registro original. |
| RN-004 | Cada modalidade de feedback tem um modo de identificação do emissor: identificado (o receptor vê quem emitiu), confidencial (a identidade fica oculta para o receptor e só o RH pode consultá-la) ou anônimo (nenhum perfil, nem RH nem administrador, consegue vincular a resposta ao emissor). O feedback do gestor para o colaborador é identificado. Na avaliação ascendente, entre pares e na equipe, o modo padrão é confidencial, e o ciclo pode ser configurado como anônimo. | RE-33; RD-15; RQ-04; RQ-13; ESC | Must | O modo confidencial protege o emissor do gestor avaliado (disposição a ser sincero com o gestor identificado: média 1,5 de 5 nos questionários) e mantém o acesso do RH pedido pela PO (E01 §11). Entre pares, a PO aceita omitir o emissor (E01 §11), e a E02 prefere o anonimato (E02 §6). |
| RN-005 | Resultados de fontes confidenciais ou anônimas (pares, equipe, 360° e avaliação ascendente) só podem ser exibidos de forma agregada e quando houver um número mínimo de respondentes, configurável, com padrão de 3. Abaixo desse mínimo, as respostas são agrupadas em outra categoria ou omitidas. | RQ-14; RD-17; RA-19 | Must | Impede identificar o emissor por exclusão. Padrão de 3 sugerido pela pesquisa documental; o 15Five usa 5. |
| RN-006 | Planos de ação e metas de desenvolvimento são definidos em conjunto pelo colaborador e pelo gestor; no plano de ação, pelo receptor e pelo emissor do feedback. | RQ-08; RE-15 | Must | Resposta idêntica nos dois questionários; o plano "é produto da colaboração dos dois" (E01 §4). |
| RN-007 | O sistema apoia o desenvolvimento das pessoas e não decide promoção, salário ou desligamento. A organização pode usar o histórico como um dos critérios dessas decisões; nesse caso, os critérios devem estar documentados e ser os mesmos para todos no mesmo cargo. | RE-34; RD-46 | Must | "Eu focaria mais no desenvolvimento da pessoa" (E01 §8); histórico como um dos critérios de promoção (E01 §10). |
| RN-008 | Indicadores, pontuações e gráficos são apoio à decisão humana. O sistema não toma decisões automáticas sobre o colaborador e, quando calcular uma pontuação, deve exibir os critérios e os dados usados no cálculo. | RD-27 | Must | LGPD, art. 20 (decisões automatizadas). |
| RN-009 | O sistema não é canal de denúncia. | RE-35; RD-48 | Must | "Não é um software de reclamações, é um software de feedbacks" (E01 §32). O atalho para o canal da organização está em RF-064. |
| RN-010 | Cada instalação do sistema atende a uma única organização. | RE-37; RD-23 | Should | A PO definiu "uma empresa específica, não um conjunto de empresas" (E01 §25). Com uma organização por instalação, o isolamento entre organizações (RD-23) deixa de ser necessário. |
| RN-011 | Feedbacks, avaliações e planos de ação são mantidos enquanto o colaborador estiver na organização e, após o desligamento, por 5 anos (prazo padrão, configurável em RF-062), ao fim dos quais são eliminados ou anonimizados. | RE-36; RD-24 | Should | Prazo dito pela PO: "talvez cinco anos" (E01 §37). A pesquisa documental aponta 2 anos de prescrição trabalhista após o desligamento (CLT, art. 11); por isso o prazo é configurável pela organização. |
| RN-012 | O consentimento não é a base legal padrão para tratar dados de feedback de empregados. O tratamento principal se apoia em execução de contrato ou legítimo interesse; o consentimento fica restrito a funcionalidades opcionais, e recusá-lo não pode bloquear o uso do sistema nem prejudicar o colaborador. | RD-03; RQ-12 | Must | LGPD, arts. 7º, 8º e 10. Ajusta o RQ-12. |
| RN-013 | Cadastros e formulários devem coletar apenas os dados necessários à finalidade de feedback e desenvolvimento. É vedado criar campos para dados pessoais sensíveis. | RD-05 | Must | LGPD, arts. 6º, III, e 11 (dados sensíveis: saúde, origem racial ou étnica, religião, opinião política, filiação sindical, vida sexual, dado genético ou biométrico). |
| RN-014 | Competências e perguntas não podem usar critérios discriminatórios, como sexo, origem, raça, cor, estado civil, situação familiar, deficiência ou idade. | RD-45 | Must | Constituição Federal, art. 7º, XXX e XXXI; Lei nº 9.029/1995. |
| RN-015 | Dados individuais de feedback não podem ser usados para monitorar a saúde do colaborador. Se a organização quiser usá-los na gestão de riscos psicossociais, só poderá fazê-lo com indicadores agregados e anonimizados. | RD-49 | Should | Boa prática derivada da LGPD (finalidade) e da NR-1. |
| RN-016 | Colaboradores menores de 18 anos, como aprendizes, devem ser identificados no cadastro, e seus dados devem ser tratados no seu melhor interesse e compartilhados apenas no estritamente necessário. | RD-29 | Must | LGPD, art. 14. |

---

## 7. Cobertura do escopo do trabalho

Cada item do enunciado e da checklist da issue #45 tem pelo menos um requisito Must.

| Item do escopo | Requisitos que o atendem |
|---|---|
| Fontes de feedback: chefe → colaborador, pares e 360° | RF-024, RF-025, RF-027, RF-030 |
| Tipos de feedback: formal, informal, positivo e construtivo | RF-013, RF-014, RF-015, RF-016, RF-022, RN-002 |
| Questionário para apoiar emissores e orientar receptores | RF-005, RF-006, RF-007, RF-008, RF-009, RF-026, RF-027 |
| Várias fontes, sempre com base em dados coletados dos emissores | RF-011, RF-023, RF-024, RF-028, RF-032, RN-001 |
| Análise robusta: tendências, números e recursos visuais | RF-032, RF-033, RF-049, RF-050, RNF-007, RNF-020 |
| Confidencialidade e anonimato | RF-019, RF-030, RN-004, RN-005, RNF-001, RNF-002, RNF-003 |
| Acompanhamento por plano de ação de melhoria | RF-042, RF-043, RF-044, RF-045, RN-006 |
| Histórico dos feedbacks | RF-048, RF-051, RN-003, RN-011 |
| Planejamento de desenvolvimento: metas e acompanhamento das melhorias | RF-023, RF-046, RF-047, RF-049, RN-006 |
| LGPD | RF-053, RF-056 a RF-060, RF-062, RNF-004, RNF-005, RNF-031, RN-012, RN-013 |
| Plataforma web | RNF-016, RNF-017, RNF-030 |
| Perspectiva de uso em dispositivos móveis | RNF-027, RNF-028 (primeira versão); RNF-035, RNF-036 (versão móvel futura) |

---

## 8. Conflitos e decisões da consolidação

Esta seção registra os pontos em que as fontes divergiam ou não davam a resposta completa, e a decisão tomada para cada um.

| # | Conflito ou questão | Fontes | Decisão | Requisitos |
|---|---|---|---|---|
| C-01 | Quem escolhe os avaliadores do 360°: o gestor ou o próprio avaliado | E01 §21 × RA-11 | Segue a PO: o gestor abre o ciclo e seleciona os participantes do seu time | RF-025 |
| C-02 | Quem cria o ciclo formal: o administrador ou o gestor | RA-09 × E01 §5, §17 | Gestor ou RH. A PO descreve o gestor planejando; o RH mantém o questionário padrão (E01 §29) | RF-022, RF-008 |
| C-03 | Quem vê o feedback: receptor, emissor e RH (E01) ou pessoa, gestor direto e RH (Q01, Q02) | RE-29 × RQ-05, RD-14 | União das duas listas. Na E02 só a gestora e a pessoa veem porque a secretaria não tem RH próprio | RNF-001 |
| C-04 | Avaliação ascendente identificada (transparência da PO) ou anônima (questionários) | E01 §11 × RQ-04, RQ-13; RD-15, RD-16 | Modo confidencial como padrão na ascendente, entre pares e na equipe: a identidade fica oculta para o avaliado e só o RH pode consultá-la, como a PO pediu. O ciclo pode ser configurado como anônimo. Como o RH vê o emissor, o padrão não pode ser chamado de "anônimo" (RD-16) | RN-004, RF-030, RF-019 |
| C-05 | O reconhecimento rápido precisa ter fato? | RA-03 × RA-24 | Sim: a própria PO exemplifica o feedback positivo com fatos (E01 §1). O formulário é simplificado, mas o fato continua obrigatório | RF-015, RN-002 |
| C-06 | Registro prévio de fatos: função própria ou campo do feedback | RA-02 | Função própria: "registro os fatos, e depois eu posso linkar" (E01 §1) | RF-011 |
| C-07 | Consentimento antes da coleta (Q01) × consentimento inadequado na relação de emprego | RQ-12 × RD-03 | Vale o RD-03. O registro de consentimento fica só para funcionalidades opcionais | RN-012, RF-055 |
| C-08 | Uma ou várias organizações no sistema | E01 §25, §31; RE-37 × RD-23 | Uma organização por instalação, que é a última posição da PO: "uma empresa específica, não um conjunto de empresas" (E01 §25). O isolamento entre organizações (RD-23) deixa de ser necessário | RN-010, RNF-029 |
| C-09 | Responder pelo celular: "nada útil" (Q01) × "muito útil" (Q02) | RQ-20 | Interface responsiva é Must, porque o enunciado exige a perspectiva móvel. O aplicativo nativo fica para a versão futura | RNF-027, RNF-035 |
| C-10 | Lembretes: "pouco útil" (Q01) × "útil" (Q02) | RQ-21 | O lembrete da sessão, pedido pela PO, é Should; os demais lembretes são Could e podem ser desativados | RF-037, RF-040 |
| C-11 | Prioridade dos indicadores (Should na síntese) | RE-07 | Must: ao planejar check-ins e indicadores, a PO destacou "aqui é importante" (E01 §5) | RF-023 |
| C-12 | Integração com sistemas externos (SSO e API de RH) | RA-23, RD-39 | Won't nesta versão: a PO aceitou planilha ou cadastro manual (E01 §30) | RF-004, RNF-025 |
| C-13 | A Diretoria vê resultados individuais? | Q02 × E01 §11, Q01 | Não. Só o Q02 incluiu a Diretoria; ela vê apenas indicadores agregados, respeitando o mínimo de respondentes | RNF-001, RN-005 |
| C-14 | O emissor pode editar um feedback já registrado? | E01 §20 × RD-47 | Sim, com versões. A PO vetou só a exclusão; cada edição gera nova versão sem apagar a anterior | RN-003 |
| C-15 | Prazo de guarda após o desligamento: 5 anos (PO) ou 2 anos (prescrição trabalhista) | E01 §37 × RD-24 | Padrão de 5 anos, como disse a PO, configurável pela organização, que pode reduzi-lo ao prazo de prescrição (CLT, art. 11) | RN-011, RF-062 |
| C-16 | O gestor pode registrar fato relatado por outro colaborador? | E02 §3 × E01 §2 (RE-31) | Sim, marcado como "relato", e só embasa um feedback depois de confirmado pela observação do gestor, como a E02 já faz (E02 §4) | RF-012, RN-001 |
| C-17 | O sistema deve sugerir horários livres para a sessão? | E02 §8 | Could: fonte única e dependente da agenda dos usuários. O agendamento com lembrete atende ao essencial | RF-038, RF-037 |
| C-18 | Consulta de problemas recorrentes por cargo após a saída do ocupante | E02 §6 × RD-49 | Could, apenas com dados agregados e sem identificar os ocupantes anteriores | RF-052 |
| C-19 | O RH pode ocultar resposta inadequada antes de liberar resultados? | RA-13 × E01 §20 | Could. Ocultar sem apagar, com auditoria e aviso ao emissor, o que preserva a regra de não exclusão | RF-035, RN-003 |
| C-20 | Número mínimo de respondentes para exibir resultados agregados | RD-17 × 15Five (5) | 3, configurável, como sugere a pesquisa documental | RN-005 |
| C-21 | O avaliado que pede acesso aos seus dados vê a identidade de emissores confidenciais? | LGPD, art. 18, II × RD-15 | Não. Recebe o conteúdo sem a identidade, porque os direitos de um titular não anulam os do outro (pesquisa documental, seção 8) | RF-056, RN-004 |
| C-22 | Check-ins periódicos para todos os colaboradores ou só para quem tem plano de ação | RA-01 | O gestor define a quem se aplicam, seguindo a PO, que prefere "não ser restritiva" e deixar a escolha ao gestor (E01 §21) | RF-041 |
| C-23 | Metas numéricas dos RNF (desempenho, disponibilidade, backup e uso) | RD-31 a RD-34; RE-30 | Adotados os valores da pesquisa documental. Para o feedback informal, adotada a meta "uma única tela" para tornar o RE-30 verificável | RNF-008, RNF-009, RNF-010, RNF-011, RNF-013 |

---

## 9. Fora do escopo

| Item | Motivo | Fonte |
|---|---|---|
| Canal de denúncia | "Denúncia é denúncia" (E01 §32). O sistema só aponta para o canal da organização | RN-009, RF-064 |
| Decisão sobre promoção, salário ou desligamento, e calibração de notas | Foco no desenvolvimento (E01 §8) | RN-007; FA-17 descartada na síntese do sistema análogo |
| Consequências para quem não responde a uma avaliação | "Está fora do escopo desse sistema" (E01 §21). O sistema só registra a ausência | RF-029 |
| Nota de bem-estar, painel de clima e pesquisa de engajamento | Aproximam-se de dados de saúde e fogem do foco em fatos | RN-015; FA-02, FA-22 e FA-23 descartadas |
| Prioridades semanais | Gestão de tarefas, fora do domínio de feedback | FA-03 descartada |
| Reconhecimento público em mural e feedback visível "somente ao gestor" | Contrariam a privacidade por padrão e o acesso do receptor ao próprio feedback (E01 §11) | RNF-002; partes de FA-05 e FA-07 descartadas |
| Avaliação de estágio probatório de servidores públicos | Segue regras de cada carreira, definidas fora da organização (E02 §2) | Síntese das entrevistas, seção 6 |
| Aplicativo móvel nativo | Versão futura; a primeira versão é web responsiva | RNF-035, RNF-036 |

---

## 10. Rastreabilidade dos requisitos candidatos

Todos os candidatos das quatro fontes estão abaixo, com o requisito definitivo para onde foram. Esta tabela é a base da rastreabilidade vertical da matriz (#49).

**Tratamentos:** *Mantido* (virou um requisito sem mudança de sentido); *Unido* (juntou-se a candidatos de outras fontes); *Dividido* (gerou mais de um requisito); *Ajustado* (mudou de conteúdo, com o motivo indicado); *Reclassificado* (mudou de tipo); *Absorvido* (a necessidade já está atendida por outro requisito).

### 10.1 Entrevistas

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RE-01 | RF-013, RN-002 | Dividido entre registro (RF) e campos obrigatórios (RN) |
| RE-02 | RF-011 | Unido a RA-02 |
| RE-03 | RF-016 | Unido a RA-21 |
| RE-04 | RF-014, RF-015 | Dividido entre feedback informal e reconhecimento simplificado |
| RE-05 | RF-012 | Mantido como Could, com a condição de confirmação pelo gestor |
| RE-06 | RF-022, RF-041 | Unido ao RA-09 e RQ-01; também origina os check-ins periódicos (RF-041) |
| RE-07 | RF-023 | Prioridade elevada para Must |
| RE-08 | RF-037 | Unido a RA-08 |
| RE-09 | RF-038 | Mantido |
| RE-10 | RF-047 | Mantido |
| RE-11 | RF-005, RF-006, RF-021 | Dividido entre competências fixas, competências específicas e vínculo do feedback à competência |
| RE-12 | RF-007, RF-008 | Dividido entre questionários reutilizáveis e questionário padrão |
| RE-13 | RF-009 | Prioridade elevada para Should |
| RE-14 | RF-010 | Mantido |
| RE-15 | RF-042, RN-006 | Dividido entre plano de ação (RF) e definição conjunta (RN) |
| RE-16 | RF-043 | Unido a RA-18 |
| RE-17 | RF-045 | Mantido |
| RE-18 | RF-024, RF-027 | Dividido entre modalidades e resposta à avaliação |
| RE-19 | RF-025, RF-027 | Unido ao RA-11, que foi corrigido; apoia também a resposta à avaliação |
| RE-20 | RF-029 | Mantido |
| RE-21 | RF-033 | Unido a RQ-18 |
| RE-22 | RF-034 | Mantido |
| RE-23 | RF-017 | Unido a RQ-03, RD-37 e RA-21; prioridade elevada para Should |
| RE-24 | RF-048, RF-049 | Dividido entre histórico e painel |
| RE-25 | RF-044, RF-050 | Dividido entre acompanhamento de planos e painel do RH |
| RE-26 | RF-052 | Mantido |
| RE-27 | RF-003 | Unido a RD-14 |
| RE-28 | RF-001, RF-002 | Dividido entre cadastro manual e importação |
| RE-29 | RNF-001 | Unido ao RQ-05 e RD-14, somando o gestor direto |
| RE-30 | RNF-013 | Ajustado para meta verificável |
| RE-31 | RN-001 | Unido a RD-44, RA-24 |
| RE-32 | RN-003 | Unido a RD-47 |
| RE-33 | RF-030, RN-004 | Unido aos modos de identificação do RD-15 |
| RE-34 | RN-007 | Unido a RD-46 |
| RE-35 | RF-064, RN-009 | Unido ao RD-48, dividido entre regra (RN) e atalho para o canal (RF) |
| RE-36 | RF-062, RN-011 | Unido ao RD-24, dividido entre política configurável (RF) e prazo padrão (RN); prazo padrão de 5 anos, conforme a PO |
| RE-37 | RN-010 | Mantido; absorve o RD-23 |

### 10.2 Questionários

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RQ-01 | RF-022 | Unido a RE-06, RA-09 |
| RQ-02 | RF-005, RF-007 | Unido às competências e aos questionários |
| RQ-03 | RF-017 | Unido a RE-23, RD-37, RA-21 |
| RQ-04 | RN-004 | Unido aos modos de identificação; ascendente confidencial por padrão |
| RQ-05 | RNF-001 | Unido ao RE-29 e RD-14; a Diretoria vê só dados agregados |
| RQ-06 | RF-031 | Unido a RA-06 |
| RQ-07 | RF-042 | Unido a RE-15, RA-18 |
| RQ-08 | RF-046, RN-006 | Unido ao RE-15 como RN; também origina as metas individuais (RF-046) |
| RQ-09 | RF-048 | Unido a RE-24, RD-47 |
| RQ-10 | RF-049 | Unido ao painel do colaborador |
| RQ-11 | RNF-014 | Mantido |
| RQ-12 | RF-055, RN-012 | Ajustado: restrito a funcionalidades opcionais (RD-03) |
| RQ-13 | RN-004 | Unido aos modos de identificação (definição do modo anônimo) |
| RQ-14 | RN-005 | Unido ao RD-17 e RA-19 |
| RQ-15 | RF-024 | Unido a RE-18, RA-10 |
| RQ-16 | RF-032, RF-050 | Mantido; também alimenta o painel do gestor e do RH |
| RQ-17 | RF-044, RF-050 | Unido ao RE-25 |
| RQ-18 | RF-033 | Unido a RE-21 |
| RQ-19 | RF-049 | Unido ao painel do colaborador |
| RQ-20 | RNF-027 | Unido ao RD-56 (interface responsiva) |
| RQ-21 | RF-040 | Mantido como Could; o lembrete da sessão está em RF-037 |

### 10.3 Pesquisa documental

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RD-01 | RF-053 | Mantido |
| RD-02 | RF-054 | Mantido |
| RD-03 | RN-012 | Mantido como RN; ajusta o RQ-12 |
| RD-04 | RF-055 | Unido a RQ-12 |
| RD-05 | RN-013 | Mantido |
| RD-06 | RF-018 | Mantido |
| RD-07 | RF-056 | Mantido |
| RD-08 | RF-057 | Mantido |
| RD-09 | RF-020 | Mantido |
| RD-10 | RF-058 | Mantido |
| RD-11 | RF-059 | Mantido |
| RD-12 | RF-060 | Mantido |
| RD-13 | RF-061 | Mantido |
| RD-14 | RF-003, RNF-001 | Unido ao RE-29 e RQ-05; apoia também o controle por perfil |
| RD-15 | RF-030, RN-004 | Dividido entre regra (RN) e configuração (RF) |
| RD-16 | RF-019 | Unido a RA-05 |
| RD-17 | RN-005 | Unido a RQ-14, RA-19 |
| RD-18 | RNF-003 | Mantido |
| RD-19 | RNF-004 | Mantido |
| RD-20 | RNF-005 | Mantido |
| RD-21 | RNF-006 | Mantido |
| RD-22 | RNF-002 | Unido ao RA-07 |
| RD-23 | RN-010 | Absorvido pelo RE-37 (uma organização por instalação) |
| RD-24 | RF-062, RN-011 | Dividido entre política configurável (RF) e prazo padrão (RN) |
| RD-25 | RNF-032 | Mantido como restrição condicional |
| RD-26 | RF-063 | Mantido |
| RD-27 | RN-008 | Mantido |
| RD-28 | RNF-033 | Mantido como restrição condicional |
| RD-29 | RN-016 | Mantido como RN |
| RD-30 | RNF-034 | Mantido como restrição |
| RD-31 | RNF-008 | Mantido |
| RD-32 | RNF-009 | Mantido |
| RD-33 | RNF-010 | Mantido |
| RD-34 | RNF-011 | Mantido |
| RD-35 | RNF-012 | Mantido |
| RD-36 | RNF-015 | Mantido |
| RD-37 | RF-017 | Unido às orientações (RE-23, RQ-03, RA-21) |
| RD-38 | RNF-024 | Mantido |
| RD-39 | RF-002, RNF-025 | Dividido: importação por planilha (Should) e API de integração (Won't) |
| RD-40 | RNF-026 | Mantido |
| RD-41 | RNF-028 | Mantido |
| RD-42 | RNF-029 | Ajustado: retirado o número de organizações |
| RD-43 | RNF-007 | Mantido |
| RD-44 | RN-001 | Unido ao RE-31 |
| RD-45 | RN-014 | Mantido |
| RD-46 | RN-007 | Unido ao RE-34 |
| RD-47 | RF-048, RF-051, RN-003 | Dividido entre não exclusão, histórico e exportação |
| RD-48 | RF-064, RN-009 | Dividido entre regra (RN) e atalho para o canal (RF) |
| RD-49 | RN-015 | Mantido |
| RD-50 | RNF-017 | Mantido |
| RD-51 | RNF-018 | Mantido |
| RD-52 | RNF-019 | Mantido |
| RD-53 | RNF-020 | Mantido |
| RD-54 | RNF-021 | Mantido |
| RD-55 | RNF-022 | Mantido |
| RD-56 | RNF-027 | Unido a RQ-20 |
| RD-57 | RNF-016, RNF-023 | Mantido; apoia também o requisito de idioma |
| RD-58 | RF-065 | Mantido |
| RD-59 | RNF-036 | Mantido como Won't (versão móvel futura) |

### 10.4 Sistema análogo

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RA-01 | RF-041 | Mantido; o gestor define a quem os check-ins se aplicam |
| RA-02 | RF-011 | Unido a RE-02 |
| RA-03 | RF-014, RF-015 | Dividido entre feedback informal e reconhecimento simplificado |
| RA-04 | RF-021 | Unido a RE-11 |
| RA-05 | RF-019 | Unido a RD-16 |
| RA-06 | RF-031 | Unido a RQ-06 |
| RA-07 | RNF-002 | Unido ao RD-22 |
| RA-08 | RF-037, RF-039 | Dividido entre agendamento (Should) e pauta com notas privadas (Could) |
| RA-09 | RF-022 | Unido ao RE-06; responsável ajustado para gestor ou RH |
| RA-10 | RF-024, RF-027 | Unido a RE-18 e RQ-15; apoia também a resposta à avaliação |
| RA-11 | RF-025 | Corrigido conforme a PO: o gestor seleciona os participantes |
| RA-12 | RF-030 | Unido a RE-33, RD-15 |
| RA-13 | RF-035 | Mantido como Could |
| RA-14 | RF-007 | Unido a RE-12, RQ-02 |
| RA-15 | RF-028 | Mantido |
| RA-16 | RF-023, RF-046 | Dividido entre metas individuais e indicadores do ciclo |
| RA-17 | RF-005, RF-006 | Unido a RE-11, dividido entre competências fixas e específicas |
| RA-18 | RF-042, RF-043 | Dividido entre criação e acompanhamento do plano |
| RA-19 | RN-005 | Unido ao RQ-14 e RD-17 |
| RA-20 | RF-049, RF-050 | Unido aos painéis |
| RA-21 | RF-016, RF-017 | Dividido entre estrutura por tipo e orientações |
| RA-22 | RNF-035 | Mantido como Won't (versão móvel futura) |
| RA-23 | RF-004 | Rebaixado para Won't (integração não pedida) |
| RA-24 | RF-013, RN-001, RN-002 | Dividido entre registro, campos obrigatórios e base em fatos |
| RA-25 | RNF-016 | Unido ao RD-57; mantido como Must |
| RA-26 | RF-036 | Reclassificado de RN para RF |

---

## 11. Limitações

- **Fontes pequenas.** São duas entrevistas e dois questionários. Falta a visão de alguém de RH, que aparece só pelo que a PO disse sobre o perfil.
- **Sem BPMN.** A issue do processo AS-IS (#44) foi desconsiderada. As dores foram tiradas das transcrições, o que limita a visão do fluxo completo do processo atual.
- **Metas numéricas.** Os valores dos RNF de desempenho, disponibilidade, backup e do feedback informal em uma tela vêm da pesquisa documental ou desta consolidação, e não de pedido da PO. Eles serão detalhados na especificação suplementar (#51).
- **Escopo amplo de propósito.** A PO pediu requisitos amplos e disse que a arquitetura pode ser reduzida, por exemplo só a gestor e colaborador (E01 §24). A redução será decidida na segunda etapa do trabalho, sem alterar esta lista.
