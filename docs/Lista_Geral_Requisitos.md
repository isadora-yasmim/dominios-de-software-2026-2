# Lista Geral de Requisitos

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #45 · **Versão:** 1.2 · **Data:** 18/11/2026
**Responsável:** Verônica Ribeiro Oliveira Palmeira
**Artefatos relacionados:** [Lista_Geral_Requisitos.csv](Lista_Geral_Requisitos.csv) (mesmos requisitos, com todos os atributos, para a matriz de rastreabilidade)

**Entradas consolidadas:**

| Fonte | Artefato | Issue |
|---|---|---|
| Entrevistas (E01 e E02) | [Síntese dos Requisitos das Entrevistas](elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md) | #41 |
| Questionários (Q01 e Q02) | [Síntese dos Requisitos dos Questionários](elicitacao/questionarios/Sintese.md) | #42 |
| Pesquisa documental | [Requisitos extraídos da Pesquisa Documental](elicitacao/pesquisa-documental/Requisitos_Pesquisa_Documental.md) | #33 |
| Sistema análogo (15Five) | [Síntese dos Requisitos do Sistema Análogo](elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md) | #43 |
| Processo atual em BPMN (AS-IS 1 e AS-IS 2) | [Processo AS-IS de feedback e avaliação, com as dores](elicitacao/bpmn/Processo_AS-IS_e_Dores.md) | #44 |
| Enunciado do trabalho | Projeto da Disciplina (área, escopo e restrições definidos pela professora) | — |

## Histórico de revisões

| Versão | Data | Descrição | Autora |
|---|---|---|---|
| 1.0 | 17/11/2026 | Versão inicial: 160 candidatos de 5 técnicas consolidados em 117 requisitos | Verônica Ribeiro Oliveira Palmeira |
| 1.1 | 17/11/2026 | Revisão final (#55): incorpora as alterações indicadas pela especificação IEEE 830 (Apêndice C.3): perfis diretoria e encarregado no RF-003 (ERS-D02), piso de 3 respondentes na RN-005 (ERS-D08) e plano de ação de feedback confidencial na RN-006 (ERS-D05). A seção 9 passa a registrar os pontos como decisões do grupo, ainda não confirmadas pela PO. Nenhum identificador, prioridade ou total foi alterado | Verônica Ribeiro Oliveira Palmeira |
| 1.2 | 18/11/2026 | Observação do RNF-006 aponta os valores já definidos na especificação suplementar (DS-05 e DS-06); textos da seção 9 e da seção 12 sem atribuir motivo à PO. Nenhum identificador, prioridade ou total foi alterado | Verônica Ribeiro Oliveira Palmeira |

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Método de consolidação](#2-método-de-consolidação)
3. [Resumo](#3-resumo)
4. [Requisitos funcionais](#4-requisitos-funcionais)
5. [Requisitos não funcionais](#5-requisitos-não-funcionais)
6. [Regras de negócio](#6-regras-de-negócio)
7. [Cobertura do escopo e das dores](#7-cobertura-do-escopo-e-das-dores)
8. [Conflitos resolvidos na consolidação](#8-conflitos-resolvidos-na-consolidação)
9. [Pontos decididos pelo grupo, sem confirmação da PO](#9-pontos-decididos-pelo-grupo-sem-confirmação-da-po)
10. [Fora do escopo](#10-fora-do-escopo)
11. [Rastreabilidade dos requisitos candidatos](#11-rastreabilidade-dos-requisitos-candidatos)
12. [Limitações](#12-limitações)

---

## 1. Objetivo

Reunir em uma única lista os requisitos levantados em todas as fontes de elicitação, sem repetições, cada um com identificador definitivo, tipo, origem e prioridade. Os conflitos entre fontes estão resolvidos (seção 8). Os pontos que dependem de confirmação da PO estão registrados com a decisão adotada nesta versão (seção 9).

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
| Processo AS-IS em BPMN (`RP`) | 17 | 25 |
| Enunciado do trabalho (`ESC`) | — | 20 |
| Transcrição, sem candidato anterior | — | 1 (RF-026) |
| **Total de candidatos** | **160** | |

**Candidatos do BPMN.** O artefato do processo AS-IS (#44) tem dois diagramas, um por entrevista, com as dores D1 a D6 marcadas em cada um, mas não numera requisitos candidatos. Para manter a rastreabilidade definida no processo (seção 5.1), esta consolidação extraiu os candidatos `RP-01` a `RP-17` das dores e das tarefas dos diagramas. Cada um aponta para o diagrama, o elemento e a dor de onde saiu (seção 11.5).

Os diagramas modelam o que foi dito nas entrevistas. Por isso os candidatos `RP` não contam como fonte independente, nem na contagem de fontes da seção 3, nem para subir a prioridade de um requisito. O BPMN serviu para três coisas:

- mostrar em que ponto do processo atual cada requisito atua;
- conferir se cada dor tem requisito que a trate (seção 7.2);
- revelar ligações que a leitura das entrevistas, tema por tema, não tinha mostrado. Duas mudaram a lista: os lembretes subiram para Should (RF-040, decisão C-09) e a regra dos modos de identificação ganhou um limite para organizações sem RH (RN-004, decisão C-14).

### 2.2 Passos

1. **Leitura das fontes.** Foram lidas as quatro sínteses, as transcrições das duas entrevistas, os dois questionários respondidos, o relatório da pesquisa documental, a descrição do 15Five, os dois diagramas BPMN com o documento que os acompanha e o enunciado do trabalho. As transcrições foram relidas para conferir a evidência de cada requisito e decidir os conflitos.
2. **Agrupamento por assunto.** Os candidatos que tratam da mesma necessidade foram reunidos em um único requisito. A coluna **Origem** lista todos os candidatos que deram origem a ele, como pede a seção 5.2 do [processo de requisitos](Processo_Requisitos.md).
3. **Separação.** Candidatos que misturavam mais de uma necessidade foram divididos, para que cada requisito descreva uma só necessidade e possa ser verificado (lista de verificação da seção 2.4 do processo).
4. **Classificação.** Cada requisito foi classificado como RF, RNF ou RN, conforme as definições da seção 5.2 do processo. Os RNF levam a característica da ISO/IEC 25010:2023. As restrições legais e de plataforma ficaram como RNF, na seção 5.10, e são tratadas na [especificação suplementar](Especificacao_Suplementar.md) (#51).
5. **Resolução de conflitos.** Quando as fontes divergiam, prevaleceu a fala da PO e, depois dela, a obrigação legal. Os conflitos resolvidos assim, ou pelos critérios do processo, estão na seção 8. Quando a PO não tratou do assunto, ou tratou sem dar uma resposta definitiva, a decisão seguiu a fonte com evidência mais forte e a opção mais protetiva para o colaborador. Esses casos estão na seção 9, como decisões do grupo ainda não confirmadas pela PO, cada uma com a justificativa.
6. **Priorização.** A prioridade proposta nas sínteses foi revista com os critérios MoSCoW do processo (seção 7), aplicados a todas as fontes ao mesmo tempo (seção 2.3).
7. **Verificação de cobertura.** Cada item do enunciado e cada dor do processo atual foram ligados aos requisitos que os atendem (seção 7). Cada candidato foi ligado ao requisito definitivo para onde foi (seção 11). Nenhum candidato ficou sem destino.

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
| **Origem** | Candidatos que deram origem ao requisito: `RE` entrevista, `RQ` questionário, `RD` pesquisa documental, `RA` sistema análogo, `RP` processo AS-IS em BPMN. `ESC` indica o enunciado do trabalho. `E01 §n` indica um trecho da transcrição usado diretamente |
| **Prioridade** | Must, Should, Could ou Won't (seção 2.3) |
| **Observações** | Evidência principal e decisões tomadas na consolidação. Quando o requisito segue uma decisão do grupo ainda não confirmada pela PO, a observação indica o ponto (seção 9) |

**Atributos comuns a todos os requisitos.** Nesta versão, todos estão com status **Aprovado** (sintetizados, classificados, priorizados e aceitos na consolidação, conforme o ciclo de vida da seção 6.2 do processo), inclusive os Won't, que ficam registrados para a versão futura. A confirmação da PO sobre os pontos da seção 9 faz parte da etapa de validação, que leva o requisito a **Validado**. A responsável pela especificação é a autora deste documento. Status e responsável estão no [CSV](Lista_Geral_Requisitos.csv), linha a linha.

**Códigos das fontes nas observações.** E01 = entrevista com a PO (Profa. Adriana); E02 = entrevista com a Secretária Municipal de Educação; Q01 e Q02 = questionários; AS-IS 1 e AS-IS 2 = diagramas BPMN do processo atual, feitos a partir da E01 e da E02; D1 a D6 = dores marcadas em cada diagrama; § = seção da transcrição ou do questionário.

**Termos usados.** As definições abaixo valem para esta lista. O glossário completo está no [Dicionário de Dados e Glossário](Dicionario_de_Dados.md) (#53).

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
| Dor | Problema do processo atual marcado no BPMN AS-IS |

---

## 3. Resumo

| Tipo | Must | Should | Could | Won't | Total |
|---|---|---|---|---|---|
| RF | 30 | 27 | 7 | 1 | 65 |
| RNF | 18 | 14 | 1 | 3 | 36 |
| RN | 13 | 3 | 0 | 0 | 16 |
| **Total** | **61** | **44** | **8** | **4** | **117** |

Dos 61 requisitos Must, 24 vêm só da pesquisa documental (obrigações da LGPD e da Lei Brasileira de Inclusão, normas de acessibilidade) ou das restrições do enunciado. Os outros 37 atendem a pedidos da PO, a itens do enunciado e ao núcleo do domínio. A proporção de Must (52% da lista) é coerente com o pedido da PO de requisitos amplos: o escopo pode ser reduzido na arquitetura, por exemplo só a gestor e colaborador (E01 §24), sem reduzir os requisitos.

| Fontes diferentes que confirmam o requisito | Quantidade |
|---|---|
| Três ou mais | 21 |
| Duas | 32 |
| Uma | 64 |

Na contagem acima, os candidatos do BPMN (`RP`) contam como entrevista, porque os diagramas foram feitos a partir das entrevistas (seção 2.1).

---

## 4. Requisitos funcionais

### 4.1 Organização, usuários e acesso

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-001 | O sistema deve permitir que o RH ou o administrador cadastre colaboradores, cargos, equipes e a hierarquia da organização (quem é gestor de quem), com quantos níveis hierárquicos forem necessários. | RE-28 | Must | Hierarquia em níveis, como professor → diretor → secretária (E02 §1). A hierarquia define o gestor direto usado em RNF-001. |
| RF-002 | O sistema deve permitir importar colaboradores, cargos, equipes e hierarquia a partir de planilha (CSV), como alternativa ao cadastro manual. | RE-28; RD-39 | Should | A PO aceita o cadastro manual quando não houver importação (E01 §30), por isso não é Must. |
| RF-003 | O sistema deve autenticar cada usuário e liberar as funções de acordo com o seu perfil: colaborador, gestor, RH, administrador, diretoria ou encarregado. A diretoria e o encarregado têm acesso restrito à sua função: a diretoria vê só indicadores agregados (RNF-001) e o encarregado atende às solicitações de titulares e aos incidentes (RF-061, RF-063). Um mesmo usuário pode acumular perfis, como o gestor que também é avaliado pelo seu superior. | RE-27; RD-14; RP-17 | Must | O acúmulo de perfis decorre da hierarquia em vários níveis (E02 §1) e da avaliação ascendente (RF-024). Em organização sem RH próprio, como a secretaria da E02, um usuário recebe o perfil RH junto com o seu (raia RH vazia no AS-IS 2), com o limite de RN-004. |
| RF-004 | O sistema deve permitir login único (SSO) com o provedor de identidade da organização. | RA-23 | Won't | Integração externa não pedida pela PO (critério Won't do processo, seção 7). |

### 4.2 Competências e questionários

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-005 | O RH ou o administrador deve poder cadastrar competências e associá-las aos cargos, formando o conjunto de competências fixas de cada cargo. | RE-11; RA-17; RQ-02 | Must | Competências fixas por cargo (E01 §9). |
| RF-006 | O gestor deve poder atribuir a um colaborador ou a um grupo competências específicas, além das competências fixas do cargo. | RE-11; RA-17; ESC | Must | "Quem tem geralmente o maior poder é o gestor" (E01 §10). O enunciado pede orientar o receptor sobre suas "competências específicas". |
| RF-007 | O sistema deve permitir criar questionários de avaliação, com perguntas vinculadas às competências e aos cargos, e salvá-los como modelos reutilizáveis em outros ciclos. | RE-12; RA-14; RQ-02; RP-02; RP-16; ESC | Must | Uso de questionário é item do enunciado. Recurso com a maior utilidade média nos questionários (4,0 de 4). |
| RF-008 | O RH deve poder definir um questionário padrão da organização, e o gestor deve poder acrescentar a ele perguntas específicas para um colaborador. | RE-12; RP-02 | Should | "Formulário pré-pronto de avaliação do RH", com outras metas para alguns indivíduos (E01 §29). |
| RF-009 | Para cada pergunta ou indicador, o sistema deve permitir escolher o tipo de resposta: escala ordinal, valor numérico, atingido/não atingido ou texto livre. | RE-13 | Should | Subiu de Could para Should: sem respostas em escala não há os números que a análise com tendências e gráficos do enunciado exige. Escala "ordinal" ou "numérica" (E01 §27). |
| RF-010 | O sistema deve permitir atribuir pesos diferentes aos feedbacks de um período e aos indicadores de um mesmo feedback no cálculo dos resultados consolidados. | RE-14 | Could | Fonte única (E01 §37). O cálculo deve exibir os critérios usados (RN-008). |

### 4.3 Registro de fatos e de feedbacks

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-011 | O emissor deve poder registrar fatos e comportamentos observados de um colaborador ao longo do período, com data e descrição, e vinculá-los depois a um ou mais feedbacks. Até o vínculo, o fato registrado é visível apenas para quem o registrou. | RE-02; RA-02; RP-01; RP-11 | Must | "Eu coleto fatos, registro os fatos, e depois eu posso linkar" (E01 §1). Resolve o ponto 1 da síntese do sistema análogo: o registro prévio é uma função própria, não só um campo do feedback. |
| RF-012 | O gestor deve poder registrar como fato um relato recebido de outro colaborador, marcado como "relato", sem que o receptor do feedback veja quem relatou. O relato só pode embasar um feedback depois de confirmado pela observação do próprio gestor. | RE-05; RP-15 | Could | A confirmação pelo gestor mantém RN-001; é o que a E02 já faz: "eu sempre procuro ver por mim mesma antes de falar com a pessoa" (E02 §4). Fonte única (E02 §3). Decisão do grupo, não confirmada pela PO: ponto P-06 (seção 9). |
| RF-013 | O sistema deve permitir registrar um feedback com emissor, receptor (colaborador ou equipe), data, tipo (positivo ou construtivo), modalidade (formal ou informal), descrição e os fatos que o motivaram. | RE-01; RA-24; RP-01; RP-11; ESC | Must | Núcleo do domínio (processo, seção 7). Campos obrigatórios em RN-002. |
| RF-014 | O sistema deve permitir registrar um feedback informal a qualquer momento, sem ciclo ou planejamento prévio, inclusive para um colaborador de outra área. | RE-04; RA-03; RP-01; ESC | Must | O informal é ad hoc, "sob demanda" (E01 §12). Feedback para pessoa de outra área (E01 §10). |
| RF-015 | O sistema deve oferecer um formulário simplificado para o feedback positivo informal (reconhecimento), que peça apenas os campos obrigatórios de RN-002. | RE-04; RA-03; RP-11 | Should | O positivo é o feedback menos frequente (E01 §20; E02 §2) e hoje é dado por WhatsApp (E02 §2). Resolve o ponto 5 da síntese do sistema análogo: o fato continua obrigatório, mas o formulário é curto. |
| RF-016 | Ao escolher o tipo do feedback, o sistema deve apresentar a estrutura correspondente. Positivo: ação ou comportamento, resultados e repercussão para o gestor, o time e a organização. Construtivo: aspecto positivo, fatos, problema, repercussão, reflexão e plano de ação. | RE-03; RA-21; RP-03; RP-05 | Should | "A pessoa escolhe essa categoria e já vem uma estrutura": "seria interessante" (E01 §16). |
| RF-017 | O sistema deve oferecer orientações sobre como dar e como receber feedback, com exemplos de feedback positivo e construtivo, disponíveis durante o registro. | RE-23; RQ-03; RD-37; RA-21; RP-03; RP-05; RP-09; RP-13 | Should | Subiu de Could para Should por aparecer em quatro fontes. "Gestores não sabem dar feedback" foi o problema citado nos dois questionários. No AS-IS 1, o RH treina quem dá e quem recebe feedback antes de implantar o processo; as orientações deixam esse conteúdo à mão no momento do registro (D3 e D5). |
| RF-018 | Nos campos de texto livre, o sistema deve orientar o emissor a descrever fatos e comportamentos observáveis e a não incluir dados sensíveis, informações de saúde ou dados de terceiros. | RD-06 | Should | Boa prática derivada da LGPD (arts. 6º, III, e 11). |
| RF-019 | Antes do envio de um feedback ou de uma avaliação, o sistema deve informar ao emissor, em linguagem clara, quem poderá ver o conteúdo e a sua identidade, conforme o modo de identificação (RN-004). | RD-16; RA-05 | Must | Transparência (LGPD, art. 6º, VI). O rótulo "anônimo" só pode ser usado no modo anônimo de RN-004. |
| RF-020 | O receptor deve poder registrar uma manifestação (réplica) sobre um feedback recebido, sem alterar o conteúdo escrito pelo emissor. | RD-09; RP-13 | Should | Boa prática derivada da LGPD (arts. 6º, V, e 18, III). |
| RF-021 | O sistema deve permitir vincular cada feedback a uma ou mais competências do receptor. | RA-04; RE-11 | Must | Necessário para a evolução por competência (RF-049) e para orientar o receptor sobre suas competências (enunciado). |

### 4.4 Ciclos formais e modalidades de feedback

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-022 | O gestor ou o RH deve poder planejar um ciclo de feedback formal, informando período, receptor (indivíduo ou equipe), objetivos de comportamento ou de resultado, competências, questionário, modalidades, participantes e datas dos check-ins. | RE-06; RA-09; RQ-01; ESC | Must | Periodicidade configurável, por exemplo de 3 ou 4 meses (E01 §5), e não só anual (Q01 §3). A PO descreve o gestor como quem planeja (E01 §5, §17); o RA-09 atribuía o ciclo só ao administrador. |
| RF-023 | Para cada objetivo de um ciclo formal, o sistema deve permitir definir indicadores, com a fonte de evidência e o valor esperado, e registrar o valor observado em cada check-in. | RE-07; RA-16; RP-16 | Must | Subiu de Should para Must: ao planejar os check-ins e os indicadores, a PO destacou "aqui é importante" (E01 §5) e os apontou como a forma de reduzir a subjetividade (E01 §29). Fontes de evidência citadas: avaliação do cliente, do setor parceiro, pontualidade das entregas (E01 §5, §14). |
| RF-024 | O sistema deve suportar as modalidades gestor → colaborador, colaborador → gestor (ascendente), entre pares, de equipe (todos avaliam todos), autoavaliação e 360°, e permitir combinar várias delas em um mesmo ciclo. | RE-18; RA-10; RQ-15; ESC | Must | Modalidades confirmadas pela PO (E01 §12) e exigidas no enunciado. A PO admite restringir a arquitetura a gestor e colaborador (E01 §24); isso não altera o requisito. |
| RF-025 | Na avaliação 360°, o gestor deve abrir o ciclo e selecionar ou convidar os participantes, que precisam ser membros do seu time. | RE-19; RA-11 | Must | Segue a PO (E01 §14, §21). O RA-11, em que o avaliado indicava os pares, foi corrigido conforme o ponto 9 da síntese das entrevistas. |
| RF-026 | Ao abrir um ciclo formal, o sistema deve notificar cada avaliado sobre os objetivos, as competências e os indicadores pelos quais será avaliado e sobre as datas dos check-ins. | E01 §29; E01 §19 | Should | Identificado na consolidação, sem candidato anterior: "é isso que eu vou estar avaliando e as pessoas vão ser notificadas sobre isso" (E01 §29); com feedback estabelecido, as pessoas "sabem o que que é esperado delas" (E01 §19). |
| RF-027 | Cada participante convidado deve poder responder, dentro do prazo do ciclo, ao questionário da modalidade em que avalia. | RE-18; RE-19; RA-10; ESC | Must | Função básica para que o questionário apoie a avaliação feita pelos emissores (enunciado). |
| RF-028 | Ao responder uma avaliação formal, o avaliador deve poder consultar os fatos e os feedbacks registrados sobre o avaliado no período do ciclo, respeitadas as regras de visibilidade. | RA-15; ESC | Should | Avaliação "baseada sempre em dados coletados dos emissores" (enunciado); reaproveitamento das informações (E01 §15). |
| RF-029 | O sistema deve registrar quem foi convidado para uma avaliação e não respondeu no prazo, e mostrar essa informação ao gestor e ao RH, sem aplicar nenhuma consequência automática. | RE-20; RP-06 | Should | "A informação que eu tenho que saber é: tal pessoa não participou"; consequências estão fora do escopo (E01 §21). |
| RF-030 | O RH ou o administrador deve poder configurar, por ciclo e por modalidade, o modo de identificação do emissor, dentro do que RN-004 permite. | RA-12; RD-15; RE-33 | Must | Entre pares e na equipe, "a gente pode parametrizar isso" (E01 §11). Decisão do grupo, não confirmada pela PO: ponto P-01 (seção 9). |
| RF-031 | O colaborador deve poder solicitar feedback a um ou mais colegas a qualquer momento, fora do ciclo formal, informando o tema e o prazo de resposta. | RQ-06; RA-06 | Should | Avaliado como "útil" nos dois questionários. |
| RF-032 | Ao encerrar um ciclo, o sistema deve consolidar automaticamente os resultados de cada avaliado por competência, por indicador e por modalidade. | RQ-16 | Should | Hoje a consolidação de um ciclo leva cerca de 1 semana (Q02). Ganho claro para gestor e RH (critério Should). |
| RF-033 | O sistema deve comparar a autoavaliação de um colaborador com a avaliação feita pelos demais avaliadores do ciclo, mostrando onde as percepções convergem ou divergem. | RE-21; RQ-18 | Should | "A minha percepção sobre a percepção dos meus colegas sobre mim" (E01 §14). |
| RF-034 | Após a sessão de feedback, o sistema deve permitir que o emissor avalie a postura do receptor (colaborativa ou reativa) e que o receptor avalie se o feedback agregou valor. | RE-22; RP-08 | Should | Serve "para a gente poder verificar se o processo de feedback está rodando" (E01 §13). |
| RF-035 | Antes da liberação dos resultados de um ciclo, o RH deve poder ocultar do avaliado uma resposta inadequada, sem apagá-la, com registro na trilha de auditoria e aviso ao emissor. | RA-13 | Could | Ideia vinda do sistema análogo. Ocultar não é excluir, o que preserva RN-003. Decisão do grupo, não confirmada pela PO: ponto P-07 (seção 9). |
| RF-036 | O sistema deve permitir alternar as perguntas dos check-ins periódicos entre um período e outro. | RA-26 | Could | Ideia vinda só do sistema análogo (usuários do 15Five repetem as respostas). Reclassificado de RN para RF, porque descreve uma função do sistema. |

### 4.5 Sessão de feedback e notificações

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-037 | O emissor deve poder agendar a sessão de feedback com data, hora, participantes e assunto, e o sistema deve enviar aos participantes um comunicado da sessão e um lembrete antes dela. | RE-08; RA-08; RP-12 | Should | A falta de horário é a maior dificuldade da E02 (E02 §2): sem horário em comum, o feedback "passa batido" (D2 do AS-IS 2). A PO pede "comunicado de sessão" e "lembrete" (E01 §5). |
| RF-038 | Ao agendar uma sessão, o sistema deve sugerir horários em que emissor e receptor estejam livres. | RE-09; RP-12 | Could | Única coisa pedida ao sistema pela E02 (E02 §8), mas fonte única e dependente de o sistema conhecer a agenda dos usuários. O essencial é atendido pelo agendamento com lembrete (RF-037). |
| RF-039 | A sessão agendada deve ter uma pauta compartilhada entre os participantes, e cada participante deve poder fazer anotações privadas, visíveis só para ele. | RA-08 | Could | Ideia vinda só do sistema análogo (critério Could). |
| RF-040 | O sistema deve enviar lembretes de avaliações pendentes, de check-ins e de prazos de planos de ação, e cada usuário deve poder desativá-los. | RQ-21; RP-06; RP-14 | Should | Subiu de Could para Should. Os questionários divergem ("pouco útil" no Q01, "útil" no Q02), mas a falta de lembrete aparece nas dores das duas entrevistas: a participação no 360° não é garantida (D6 do AS-IS 1, E01 §21) e o acompanhamento depende da memória (D4 do AS-IS 2). A E02 usa um caderninho "pra não esquecer de chamar alguém pra conversar" (E02 §2). O lembrete da sessão está em RF-037. |
| RF-041 | O sistema deve permitir registrar check-ins periódicos entre gestor e colaborador, com frequência configurável, vinculados às metas e aos planos de ação em andamento. O gestor define para quais colaboradores da sua equipe os check-ins periódicos valem. | RA-01; RE-06; RP-07 | Should | O gestor decide a quem se aplicam, seguindo a PO: "eu prefiro assim não ser restritiva", e o gestor "verifica o que que ele acha que é melhor" (E01 §21). Os check-ins do ciclo formal estão em RF-022 e RF-023. Decisão do grupo, não confirmada pela PO: ponto P-09 (seção 9). |

### 4.6 Plano de ação e metas de desenvolvimento

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-042 | A partir de um feedback construtivo, o sistema deve permitir criar um plano de ação com ações, responsáveis, metas, pontos de monitoramento e data final. | RE-15; RA-18; RQ-07; RP-14; ESC | Must | Plano construído em conjunto (RN-006). Recurso com utilidade média 4,0 nos questionários. Plano de ação de melhoria é item do enunciado. |
| RF-043 | O sistema deve permitir acompanhar o plano de ação: registrar o resultado de cada ponto de monitoramento, ajustar as ações e, na data final, registrar se houve melhora ou se é necessário um novo feedback. | RE-16; RA-18; RP-04; RP-07; RP-14; ESC | Must | Sem esse registro "eu não tenho controle se houve uma melhora" (E01 §6). É a decisão "Melhorou até a data final?" do AS-IS 1, que hoje fica sem controle (D4). |
| RF-044 | O gestor deve poder acompanhar o andamento dos planos de ação da sua equipe, e o RH, os de toda a organização. | RQ-17; RE-25 | Should | "Planos de ação em andamento" é o que a gestora do Q02 mais precisa acompanhar; "o RH tem que ter esse controle" (E01 §10). |
| RF-045 | O sistema deve permitir consultar quais feedbacks e planos de ação resultaram em melhora do colaborador. | RE-17; RP-04 | Should | "Quais são os feedbacks que tiveram um bom desempenho" (E01 §4). |
| RF-046 | O colaborador e o gestor devem poder cadastrar metas de desenvolvimento individuais, com descrição, competência relacionada, indicador, valor esperado e prazo, e atualizar o progresso ao longo do tempo. | RA-16; RQ-08; ESC | Must | Planejamento de desenvolvimento com metas é item do enunciado. Definição conjunta em RN-006. |
| RF-047 | O gestor e a equipe devem poder cadastrar metas da equipe para um período, como um bimestre, e registrar se foram atingidas. | RE-10 | Should | Metas bimestrais definidas com autonomia das equipes (E02 §7). |

### 4.7 Histórico, painéis e análise

| ID | Requisito | Origem | Prioridade | Observações |
|---|---|---|---|---|
| RF-048 | O sistema deve manter o histórico de cada colaborador, com os feedbacks recebidos, as avaliações, os planos de ação e as metas, em ordem cronológica. | RE-24; RQ-09; RD-47; RP-01; RP-10; RP-11; ESC | Must | "Guarda histórico dos feedbacks" (enunciado). Hoje não existe histórico (E02 §7). |
| RF-049 | O sistema deve oferecer ao colaborador um painel com a evolução de cada indicador e de cada competência ao longo do tempo, em gráficos; seus pontos fortes e pontos a melhorar; o andamento de suas metas e planos de ação; e os comentários recebidos. | RE-24; RQ-10; RQ-19; RA-20; ESC | Must | Análise com tendências, números e recursos visuais (enunciado). Todo gráfico atende a RNF-007 e RNF-020. |
| RF-050 | O sistema deve oferecer ao gestor, para a sua equipe, e ao RH, para a organização, um painel com indicadores consolidados, tendências ao longo do tempo e a situação dos planos de ação e das metas. | RE-25; RQ-16; RQ-17; RA-20; ESC | Should | Dados de fontes confidenciais ou anônimas obedecem a RN-005. |
| RF-051 | O RH deve poder exportar o histórico de um colaborador em relatório. | RD-47; RP-10 | Should | O histórico resguarda a organização juridicamente (E01 §32). |
| RF-052 | O sistema deve permitir consultar os problemas recorrentes associados a um cargo, mesmo depois que o ocupante saiu, apenas de forma agregada e sem identificar os ocupantes anteriores. | RE-26 | Could | Fonte única. "Às vezes os problemas estão relacionados ao cargo em si, não à pessoa" (E02 §6). Decisão do grupo, não confirmada pela PO: ponto P-08 (seção 9). |

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
| RF-062 | O sistema deve permitir configurar a política de retenção por categoria de dado (feedbacks, planos de ação, registros de acesso), com eliminação ou anonimização automática ao fim do prazo, inclusive após o desligamento, e com bloqueio da eliminação quando houver processo judicial em curso. | RD-24; RE-36 | Must | LGPD, arts. 15 e 16. O prazo padrão está em RN-011. Decisão do grupo, não confirmada pela PO: ponto P-05 (seção 9). |
| RF-063 | O sistema deve apoiar a gestão de incidentes de segurança: alertar eventos suspeitos, registrar o incidente (data, dados e titulares afetados, medidas adotadas), gerar a lista de titulares a comunicar e guardar o registro por no mínimo 5 anos. | RD-26 | Should | Dever do controlador que o sistema apoia: comunicar a ANPD e os titulares em até 3 dias úteis (LGPD, art. 48; Res. CD/ANPD nº 15/2024). |
| RF-064 | O sistema deve exibir um atalho visível para o canal de denúncias da organização e orientar o usuário a usá-lo quando o relato for de assédio ou de conduta grave. | RD-48; RE-35 | Should | Lei nº 14.457/2022, art. 23, para organizações obrigadas a ter CIPA. Complementa RN-009. |
| RF-065 | O sistema deve exibir o símbolo de acessibilidade em destaque e uma página de declaração de acessibilidade com o nível de conformidade e um canal para reportar barreiras. | RD-58 | Must | Lei Brasileira de Inclusão, art. 63, §1º. |

---

## 5. Requisitos não funcionais

### 5.1 Segurança

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-001 | Um feedback e o resultado de avaliação de um colaborador só podem ser vistos pelo próprio colaborador, pelo emissor (apenas o conteúdo que ele escreveu), pelo gestor direto do colaborador e pelo RH. A diretoria da organização vê apenas indicadores agregados, conforme RN-005. | Segurança (confidencialidade) | RE-29; RQ-05; RD-14 | Must | Une a E01 (receptor, emissor e RH, §11) e os questionários (pessoa, gestor direto e RH). Só o Q02 incluiu a Diretoria; por isso ela vê apenas dados agregados (necessidade, LGPD, art. 6º, III). Decisão do grupo, não confirmada pela PO: ponto P-02 (seção 9). |
| RNF-002 | Todo feedback novo deve ficar visível apenas ao público mínimo de RNF-001. A visibilidade é definida no envio e só pode ser ampliada por nova ação explícita do emissor. | Segurança (confidencialidade) | RD-22; RA-07 | Must | Privacidade por padrão (LGPD, arts. 46, §2º, e 49). O RA-07 foi unido a este requisito. |
| RNF-003 | Nos feedbacks e avaliações em modo confidencial, o vínculo entre emissor e resposta deve ser armazenado separado do conteúdo (pseudonimização), com acesso restrito ao RH e registrado na trilha de auditoria. | Segurança (confidencialidade, responsabilização) | RD-18 | Should | Boa prática derivada da LGPD (art. 13, §4º). |
| RNF-004 | Dados pessoais e conteúdo de feedback devem ser criptografados em trânsito (TLS 1.2 ou superior) e em repouso. | Segurança (confidencialidade, integridade) | RD-19 | Must | Medida técnica de segurança (LGPD, art. 46). |
| RNF-005 | O sistema deve manter trilha de auditoria inalterável dos acessos e das alterações a dados pessoais e feedbacks (quem, quando, o quê e de onde), incluindo toda consulta à identidade de emissores confidenciais. | Segurança (responsabilização, não repúdio) | RD-20 | Must | LGPD, arts. 6º, X, 37 e 46. |
| RNF-006 | O sistema deve exigir autenticação em dois fatores para RH e administradores, bloquear o acesso após tentativas sucessivas de login sem sucesso e encerrar a sessão após um período de inatividade. | Segurança (autenticidade, resistência) | RD-21 | Should | Boa prática derivada da LGPD (art. 46). Número de tentativas e tempo de inatividade definidos na especificação suplementar (#51): decisões DS-05 e DS-06. |

### 5.2 Adequação funcional

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-007 | Toda média, tendência ou gráfico exibido deve informar o período e o número de respostas que o compõem. | Adequação funcional (correção); Capacidade de interação (autodescritividade) | RD-43 | Should | Evita conclusões sobre poucos dados (LGPD, art. 6º, V). |

### 5.3 Eficiência de desempenho

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-008 | As telas principais (painel, formulário de feedback e histórico) devem carregar em até 3 s e o envio de um feedback deve ser confirmado em até 2 s, no percentil 95, em conexão 4G. | Eficiência de desempenho (comportamento temporal) | RD-31 | Should | Meta proposta pela pesquisa documental; detalhada na especificação suplementar (#51). Decisão do grupo, não confirmada pela PO: ponto P-10 (seção 9). |
| RNF-009 | O sistema deve suportar o pico de um ciclo formal, quando a maior parte dos colaboradores responde na mesma semana, sem descumprir RNF-008. | Eficiência de desempenho (capacidade) | RD-32 | Should | O volume de usuários foi dimensionado na especificação suplementar (#51, decisão DS-01). Decisão do grupo, não confirmada pela PO: ponto P-10 (seção 9). |

### 5.4 Confiabilidade

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-010 | O sistema deve ter disponibilidade mínima de 99,5% ao mês, com janelas de manutenção comunicadas com antecedência e fora dos prazos dos ciclos de avaliação. | Confiabilidade (disponibilidade) | RD-33 | Should | Meta proposta pela pesquisa documental. Decisão do grupo, não confirmada pela PO: ponto P-10 (seção 9). |
| RNF-011 | O sistema deve ter backups criptografados diários, com perda máxima de 24 h de dados (RPO), restauração em até 4 h (RTO) e testes periódicos de restauração. | Confiabilidade (recuperabilidade) | RD-34 | Should | Meta proposta pela pesquisa documental. Decisão do grupo, não confirmada pela PO: ponto P-10 (seção 9). |
| RNF-012 | Respostas a feedbacks e questionários devem ser salvas automaticamente como rascunho, para que nada se perca em caso de queda de conexão, sessão expirada ou campos obrigatórios ainda em branco. | Confiabilidade (tolerância a falhas); Capacidade de interação (proteção contra erro do usuário) | RD-35 | Should | A PO relatou um sistema que descartava o cadastro incompleto (E01 §33). |

### 5.5 Capacidade de interação

| ID | Requisito | Característica ISO/IEC 25010 | Origem | Prioridade | Observações |
|---|---|---|---|---|---|
| RNF-013 | O registro de um feedback informal deve caber em uma única tela, com apenas os campos obrigatórios de RN-002. | Capacidade de interação (operabilidade) | RE-30 | Should | Ficar "horas preenchendo informações" atrapalharia (E02 §8); dar feedback "dá trabalho" (E01 §9). A meta "uma única tela" foi definida na consolidação para tornar o RE-30 verificável. Decisão do grupo, não confirmada pela PO: ponto P-10 (seção 9). |
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
| RNF-024 | Antes do envio, o sistema deve sinalizar ao emissor termos potencialmente ofensivos ou discriminatórios e sugerir a revisão, sem bloquear o envio. | Proteção (alerta de perigo) | RD-38 | Could | Proposto só pela pesquisa documental. Trata a mesma dor do feedback dado com "uma dose de agressividade" (E01 §20; D5 do AS-IS 1), já atendida pelas orientações ao emissor (RF-017); por isso fica como Could. |

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
| RN-003 | Um feedback registrado não pode ser excluído, porque é registro oficial do histórico do colaborador. O emissor pode editá-lo, e cada alteração gera uma nova versão datada, sem apagar a anterior. | RE-32; RD-47 | Must | "Deletar não dá... aquilo ali é uma informação oficial" (E01 §20). A PO vetou só a exclusão; a edição com versões (RD-47) corrige erros sem perder o registro original. Decisão do grupo, não confirmada pela PO: ponto P-04 (seção 9). |
| RN-004 | Cada modalidade de feedback tem um modo de identificação do emissor: identificado (o receptor vê quem emitiu), confidencial (a identidade fica oculta para o receptor e só o RH pode consultá-la) ou anônimo (nenhum perfil, nem RH nem administrador, consegue vincular a resposta ao emissor). O feedback do gestor para o colaborador é identificado. Na avaliação ascendente, entre pares e na equipe, o modo padrão é confidencial, e o ciclo pode ser configurado como anônimo. Um usuário com perfil RH nunca pode consultar a identidade dos emissores das avaliações em que ele próprio é o avaliado. | RE-33; RD-15; RQ-04; RQ-13; RP-17; ESC | Must | O modo confidencial protege o emissor do gestor avaliado (disposição a ser sincero com o gestor identificado: média 1,5 de 5 nos questionários) e mantém o acesso do RH pedido pela PO (E01 §11). Entre pares, a PO aceita omitir o emissor (E01 §11), e a E02 prefere o anonimato (E02 §6). A última frase evita que o gestor que acumula o perfil RH descubra quem o avaliou (decisão C-14). Decisão do grupo, não confirmada pela PO: ponto P-01 (seção 9). |
| RN-005 | Resultados de fontes confidenciais ou anônimas (pares, equipe, 360° e avaliação ascendente) só podem ser exibidos de forma agregada e quando houver um número mínimo de respondentes, configurável, com padrão de 3 e nunca menor que 3. Abaixo desse mínimo, as respostas são agrupadas em outra categoria ou omitidas. | RQ-14; RD-17; RA-19 | Must | Impede identificar o emissor por exclusão. Padrão de 3 sugerido pela pesquisa documental; o 15Five usa 5. Decisão do grupo, não confirmada pela PO: ponto P-03 (seção 9). |
| RN-006 | Planos de ação e metas de desenvolvimento são definidos em conjunto pelo colaborador e pelo gestor; no plano de ação, pelo receptor e pelo emissor do feedback. Se o feedback de origem for confidencial, o plano é definido pelo receptor e pelo seu gestor direto, sem o emissor. | RQ-08; RE-15 | Must | Resposta idêntica nos dois questionários; o plano "é produto da colaboração dos dois" (E01 §4). |
| RN-007 | O sistema apoia o desenvolvimento das pessoas e não decide promoção, salário ou desligamento. A organização pode usar o histórico como um dos critérios dessas decisões; nesse caso, os critérios devem estar documentados e ser os mesmos para todos no mesmo cargo. | RE-34; RD-46; RP-10 | Must | "Eu focaria mais no desenvolvimento da pessoa" (E01 §8); histórico como um dos critérios de promoção (E01 §10). |
| RN-008 | Indicadores, pontuações e gráficos são apoio à decisão humana. O sistema não toma decisões automáticas sobre o colaborador e, quando calcular uma pontuação, deve exibir os critérios e os dados usados no cálculo. | RD-27 | Must | LGPD, art. 20 (decisões automatizadas). |
| RN-009 | O sistema não é canal de denúncia. | RE-35; RD-48 | Must | "Não é um software de reclamações, é um software de feedbacks" (E01 §32). O atalho para o canal da organização está em RF-064. |
| RN-010 | Cada instalação do sistema atende a uma única organização. | RE-37; RD-23 | Should | A PO definiu "uma empresa específica, não um conjunto de empresas" (E01 §25). Com uma organização por instalação, o isolamento entre organizações (RD-23) deixa de ser necessário. |
| RN-011 | Feedbacks, avaliações e planos de ação são mantidos enquanto o colaborador estiver na organização e, após o desligamento, por 5 anos (prazo padrão, configurável em RF-062), ao fim dos quais são eliminados ou anonimizados. | RE-36; RD-24 | Should | Prazo dito pela PO: "talvez cinco anos" (E01 §37). A pesquisa documental aponta 2 anos de prescrição trabalhista após o desligamento (CLT, art. 11); por isso o prazo é configurável pela organização. Decisão do grupo, não confirmada pela PO: ponto P-05 (seção 9). |
| RN-012 | O consentimento não é a base legal padrão para tratar dados de feedback de empregados. O tratamento principal se apoia em execução de contrato ou legítimo interesse; o consentimento fica restrito a funcionalidades opcionais, e recusá-lo não pode bloquear o uso do sistema nem prejudicar o colaborador. | RD-03; RQ-12 | Must | LGPD, arts. 7º, 8º e 10. Ajusta o RQ-12. |
| RN-013 | Cadastros e formulários devem coletar apenas os dados necessários à finalidade de feedback e desenvolvimento. É vedado criar campos para dados pessoais sensíveis. | RD-05 | Must | LGPD, arts. 6º, III, e 11 (dados sensíveis: saúde, origem racial ou étnica, religião, opinião política, filiação sindical, vida sexual, dado genético ou biométrico). |
| RN-014 | Competências e perguntas não podem usar critérios discriminatórios, como sexo, origem, raça, cor, estado civil, situação familiar, deficiência ou idade. | RD-45 | Must | Constituição Federal, art. 7º, XXX e XXXI; Lei nº 9.029/1995. |
| RN-015 | Dados individuais de feedback não podem ser usados para monitorar a saúde do colaborador. Se a organização quiser usá-los na gestão de riscos psicossociais, só poderá fazê-lo com indicadores agregados e anonimizados. | RD-49 | Should | Boa prática derivada da LGPD (finalidade) e da NR-1. |
| RN-016 | Colaboradores menores de 18 anos, como aprendizes, devem ser identificados no cadastro, e seus dados devem ser tratados no seu melhor interesse e compartilhados apenas no estritamente necessário. | RD-29 | Must | LGPD, art. 14. |

---

## 7. Cobertura do escopo e das dores

### 7.1 Escopo do trabalho

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

### 7.2 Dores do processo atual (BPMN AS-IS)

Cada uma das 12 dores marcadas nos dois diagramas tem pelo menos um requisito que a trata. Os candidatos de cada dor estão na seção 11.5.

| Dor | AS-IS 1 (E01, PO) | AS-IS 2 (E02, Secretaria) | Requisitos que tratam |
|---|---|---|---|
| D1 | Registro manual, em papel ou Excel; o informal fica só na conversa | Sem registro, tudo de boca; caderninho só às vezes | RF-011, RF-013, RF-014, RF-015, RF-048 |
| D2 | Planejar e acompanhar cada pessoa dá trabalho e falta tempo | As agendas não coincidem e o feedback passa batido | AS-IS 1: RF-007, RF-008. AS-IS 2: RF-037, RF-038 |
| D3 | Reação defensiva: o feedback é visto como crítica | A pessoa se justifica e vira discussão | RF-016, RF-017, RF-020 |
| D4 | Sem controle se a pessoa melhorou | O acompanhamento depende da memória e do caderninho | RF-040, RF-042, RF-043, RF-045 |
| D5 | Feedback mal dado: pouco elogio e crítica agressiva | Quem reclama fica anônimo só pela discrição da secretária | AS-IS 1: RF-016, RF-017. AS-IS 2: RF-012 |
| D6 | A participação dos avaliadores no 360° não é garantida | Sem formulário nem indicadores: avaliação pela percepção | AS-IS 1: RF-029, RF-040. AS-IS 2: RF-007, RF-023 |

Os códigos D1 a D6 são numerados em cada diagrama de forma independente. Por isso a mesma linha pode juntar dores diferentes nos dois diagramas.

---

## 8. Conflitos resolvidos na consolidação

Esta seção registra os pontos em que as fontes divergiam e que foram resolvidos na consolidação: pela fala da PO, por obrigação legal ou pelos critérios do processo. Os pontos em que as fontes não davam uma resposta definitiva estão na seção 9.

| # | Conflito ou questão | Fontes | Decisão | Requisitos |
|---|---|---|---|---|
| C-01 | Quem escolhe os avaliadores do 360°: o gestor ou o próprio avaliado | E01 §21 × RA-11 | Segue a PO: o gestor abre o ciclo e seleciona os participantes do seu time | RF-025 |
| C-02 | Quem cria o ciclo formal: o administrador ou o gestor | RA-09 × E01 §5, §17 | Gestor ou RH. A PO descreve o gestor planejando, como também mostra o AS-IS 1; o RH mantém o questionário padrão (E01 §29) | RF-022, RF-008 |
| C-03 | Quem vê o feedback: receptor, emissor e RH (E01) ou pessoa, gestor direto e RH (Q01, Q02) | RE-29 × RQ-05, RD-14 | União das duas listas. Na E02 só a gestora e a pessoa veem porque a secretaria não tem RH próprio | RNF-001 |
| C-04 | O reconhecimento rápido precisa ter fato? | RA-03 × RA-24 | Sim: a própria PO exemplifica o feedback positivo com fatos (E01 §1). O formulário é simplificado, mas o fato continua obrigatório | RF-015, RN-002 |
| C-05 | Registro prévio de fatos: função própria ou campo do feedback | RA-02 | Função própria: "registro os fatos, e depois eu posso linkar" (E01 §1) | RF-011 |
| C-06 | Consentimento antes da coleta (Q01) × consentimento inadequado na relação de emprego | RQ-12 × RD-03 | Vale o RD-03. O registro de consentimento fica só para funcionalidades opcionais | RN-012, RF-055 |
| C-07 | Uma ou várias organizações no sistema | E01 §25, §31; RE-37 × RD-23 | Uma organização por instalação, que é a última posição da PO: "uma empresa específica, não um conjunto de empresas" (E01 §25). O isolamento entre organizações (RD-23) deixa de ser necessário | RN-010, RNF-029 |
| C-08 | Responder pelo celular: "nada útil" (Q01) × "muito útil" (Q02) | RQ-20 | Interface responsiva é Must, porque o enunciado exige a perspectiva móvel. O aplicativo nativo fica para a versão futura | RNF-027, RNF-035 |
| C-09 | Lembretes: "pouco útil" (Q01) × "útil" (Q02) | RQ-21; RP-06, RP-14 | Should, e cada usuário pode desativá-los. As dores das duas entrevistas desempatam: a participação no 360° não é garantida (D6 do AS-IS 1) e o acompanhamento depende da memória (D4 do AS-IS 2), a ponto de a E02 usar um caderninho "pra não esquecer de chamar alguém pra conversar" (E02 §2) | RF-040, RF-037 |
| C-10 | Prioridade dos indicadores (Should na síntese) | RE-07 | Must: ao planejar check-ins e indicadores, a PO destacou "aqui é importante" (E01 §5) | RF-023 |
| C-11 | Integração com sistemas externos (SSO e API de RH) | RA-23, RD-39 | Won't nesta versão: a PO aceitou planilha ou cadastro manual (E01 §30) | RF-004, RNF-025 |
| C-12 | O sistema deve sugerir horários livres para a sessão? | E02 §8; RP-12 | Could: pedido de uma única fonte e dependente de o sistema conhecer a agenda dos usuários (critério Could do processo). O agendamento com lembrete atende ao essencial | RF-038, RF-037 |
| C-13 | O avaliado que pede acesso aos seus dados vê a identidade de emissores confidenciais? | LGPD, art. 18, II × RD-15 | Não. Recebe o conteúdo sem a identidade, porque os direitos de um titular não anulam os do outro (pesquisa documental, seção 8) | RF-056, RN-004 |
| C-14 | Em organização sem RH próprio, quem fica com as funções do RH, e o que acontece se for o próprio gestor | AS-IS 2 (raia RH sem tarefas; E02 §1) × RN-004, RNF-001 | Um usuário da organização recebe o perfil RH junto com o seu (RF-003). Se ele também for avaliado, por exemplo pela equipe na avaliação ascendente, não pode consultar a identidade de quem o avaliou. Sem esse limite, o modo confidencial deixaria de proteger o emissor justamente diante do gestor | RF-003, RN-004 |

---

## 9. Pontos decididos pelo grupo, sem confirmação da PO

Nos pontos abaixo, as fontes não dão uma resposta definitiva: a PO não tratou do assunto, tratou sem fechar a questão, ou as fontes divergem sem que uma prevaleça pelos critérios da seção 2.2. Pela seção 4.3 do processo, esses pontos são levados à PO. Para que a especificação não ficasse incompleta até a validação, o grupo adotou uma decisão para cada um.

Cada ponto tem a **decisão do grupo, ainda não confirmada pela PO**, com a justificativa, e os requisitos afetados estão escritos de acordo com ela. A coluna Observações desses requisitos indica o ponto correspondente. As decisões continuam sujeitas à confirmação da PO, que leva os requisitos afetados ao status **Validado** (seção 2.4). Se a PO decidir de outra forma, a mudança segue a gestão de mudanças do processo (seção 9): análise de impacto pela matriz de rastreabilidade (#49) e atualização desta lista por PR.

| # | Ponto | O que as fontes dizem | Decisão do grupo | Justificativa | Requisitos |
|---|---|---|---|---|---|
| P-01 | Na avaliação ascendente, entre pares e na equipe, o emissor fica confidencial (o RH pode saber quem é) ou anônimo (ninguém pode)? | A PO prefere transparência e quer que o RH possa saber quem emitiu (E01 §11). Os questionários pedem anonimato na avaliação do gestor: disposição a ser sincero com o gestor identificado de 1,5 em 5. A E02 prefere anonimato entre equipes (E02 §6) e hoje protege quem reclama só pela própria discrição (D5 do AS-IS 2) | Confidencial como padrão. Anônimo como opção configurável por ciclo, sempre com o mínimo de respondentes | Protege o emissor diante do gestor avaliado, como pedem os questionários, sem tirar do RH o acesso que a PO pediu. A opção anônima atende a quem prefere anonimato. Como o RH pode saber quem emitiu, o padrão não pode ser chamado de "anônimo" (RD-16) | RN-004, RF-030 |
| P-02 | A diretoria da organização pode ver resultados individuais? | Só o Q02 incluiu a Diretoria entre quem vê o resultado. A PO cita o receptor, o emissor e o RH (E01 §11); o Q01, a pessoa, o gestor direto e o RH | A diretoria vê apenas indicadores agregados, com o mínimo de respondentes | Dá a visão gerencial sem expor o colaborador a quem não é seu gestor direto (princípio da necessidade, LGPD, art. 6º, III) | RNF-001 |
| P-03 | Qual o número mínimo de respondentes para exibir resultados de fontes confidenciais ou anônimas? | A pesquisa documental sugere 3 (RD-17). O 15Five usa 5 | 3, configurável pela organização | É o menor valor que ainda impede descobrir o emissor por exclusão. Com 5, setores pequenos como os da E02, de 1 a 5 pessoas (E02 §1), ficariam sem resultado | RN-005 |
| P-04 | O emissor pode editar um feedback já registrado? | A PO disse que o feedback não pode ser excluído, porque é registro oficial (E01 §20), mas não tratou da edição. A pesquisa documental pede versionamento (RD-47) | Pode editar. Cada edição gera uma nova versão datada, sem apagar a anterior | Permite corrigir um texto mal escrito, preocupação levantada na própria entrevista (E01 §20), sem perder o registro original que a PO quer preservar | RN-003 |
| P-05 | Por quanto tempo os dados ficam guardados após o desligamento? | PO: "talvez cinco anos" (E01 §37). Pesquisa documental: 2 anos, prazo de prescrição trabalhista após o desligamento (CLT, art. 11) | 5 anos como padrão, configurável pela organização | Segue o valor dito pela PO. A configuração permite à organização reduzir o prazo ao da prescrição, conforme a sua política de retenção | RN-011, RF-062 |
| P-06 | O gestor pode registrar como fato um relato recebido de outro colaborador? | A E02 recebe relatos de colegas e não revela quem reclamou (E02 §3; D5 do AS-IS 2). A PO exige que o feedback se baseie em fatos observados (E01 §2, §20) | Pode, como fato marcado "relato", com a identidade de quem relatou oculta ao receptor. O relato só embasa um feedback depois de confirmado pela observação do próprio gestor. Prioridade Could | Mantém a base em fatos exigida pela PO (RN-001) e reproduz a prática da E02: "eu sempre procuro ver por mim mesma antes de falar com a pessoa" (E02 §4) | RF-012 |
| P-07 | O RH pode ocultar do avaliado uma resposta inadequada antes de liberar os resultados? | Prática do 15Five (RA-13). A PO disse que o feedback não pode ser apagado e citou gestores que dão feedback de forma grosseira (E01 §20) | Pode ocultar, sem apagar, com registro na trilha de auditoria e aviso ao emissor. Prioridade Could | Protege o avaliado de conteúdo agressivo sem violar a regra de não exclusão (RN-003) | RF-035 |
| P-08 | Pode haver consulta de problemas recorrentes por cargo, depois que o ocupante saiu? | Pedido só da E02 (E02 §6) | Pode, apenas com dados agregados e sem identificar os ocupantes anteriores. Prioridade Could | Atende à necessidade sem expor quem deixou o cargo (princípios da finalidade e da necessidade, LGPD, art. 6º, I e III) | RF-052 |
| P-09 | Os check-ins periódicos valem para todos os colaboradores ou só para quem tem plano de ação aberto? | O 15Five aplica os check-ins a todos (RA-01). A síntese do sistema análogo deixou a questão em aberto | O gestor define para quais colaboradores da sua equipe os check-ins valem | Segue a preferência da PO por "não ser restritiva" e deixar a escolha ao gestor (E01 §21). A frase foi dita sobre o 360° e aplicada aqui por analogia | RF-041 |
| P-10 | As metas numéricas dos RNF estão adequadas? | Os valores de desempenho, disponibilidade e backup vêm da pesquisa documental (RD-31 a RD-34). A meta de uma única tela para o feedback informal vem desta consolidação (RE-30) | Adotar esses valores nesta versão | Sem meta numérica o RNF não pode ser verificado (lista de verificação da seção 2.4 do processo). Os valores estão detalhados na especificação suplementar (#51), junto com o volume de usuários (DS-01) | RNF-008, RNF-009, RNF-010, RNF-011, RNF-013 |

---

## 10. Fora do escopo

| Item | Motivo | Fonte |
|---|---|---|
| Canal de denúncia | "Denúncia é denúncia" (E01 §32). O sistema só aponta para o canal da organização | RN-009, RF-064 |
| Decisão sobre promoção, salário ou desligamento, e calibração de notas | Foco no desenvolvimento (E01 §8). O RH consulta o histórico para decidir (AS-IS 1), mas a decisão é humana | RN-007; FA-17 descartada na síntese do sistema análogo |
| Consequências para quem não responde a uma avaliação | "Está fora do escopo desse sistema" (E01 §21). O sistema só registra a ausência | RF-029 |
| Treinamento de quem dá e de quem recebe feedback | Atividade do RH ao implantar o processo (E01 §13; AS-IS 1). O sistema apoia com orientações e exemplos | RF-017 |
| Nota de bem-estar, painel de clima e pesquisa de engajamento | Aproximam-se de dados de saúde e fogem do foco em fatos | RN-015; FA-02, FA-22 e FA-23 descartadas |
| Prioridades semanais | Gestão de tarefas, fora do domínio de feedback | FA-03 descartada |
| Reconhecimento público em mural e feedback visível "somente ao gestor" | Contrariam a privacidade por padrão e o acesso do receptor ao próprio feedback (E01 §11) | RNF-002; partes de FA-05 e FA-07 descartadas |
| Avaliação de estágio probatório de servidores públicos | Segue regras de cada carreira, definidas fora da organização (E02 §2). Também fica fora do fluxo no AS-IS 2 | Síntese das entrevistas, seção 6; anotação do AS-IS 2 |
| Aplicativo móvel nativo | Versão futura; a primeira versão é web responsiva | RNF-035, RNF-036 |

---

## 11. Rastreabilidade dos requisitos candidatos

Todos os candidatos das cinco fontes estão abaixo, com o requisito definitivo para onde foram. Esta tabela é a base da rastreabilidade vertical da matriz (#49).

**Tratamentos:** *Mantido* (virou um requisito sem mudança de sentido); *Unido* (juntou-se a candidatos de outras fontes); *Dividido* (gerou mais de um requisito); *Ajustado* (mudou de conteúdo, com o motivo indicado); *Reclassificado* (mudou de tipo); *Absorvido* (a necessidade já está atendida por outro requisito).

### 11.1 Entrevistas

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RE-01 | RF-013, RN-002 | Dividido entre registro (RF) e campos obrigatórios (RN) |
| RE-02 | RF-011 | Unido a RA-02, RP-01, RP-11 |
| RE-03 | RF-016 | Unido a RA-21, RP-03, RP-05 |
| RE-04 | RF-014, RF-015 | Dividido entre feedback informal e reconhecimento simplificado |
| RE-05 | RF-012 | Mantido como Could, com a condição de confirmação pelo gestor |
| RE-06 | RF-022, RF-041 | Unido ao RA-09 e RQ-01; também origina os check-ins periódicos (RF-041) |
| RE-07 | RF-023 | Prioridade elevada para Must |
| RE-08 | RF-037 | Unido a RA-08, RP-12 |
| RE-09 | RF-038 | Unido a RP-12 |
| RE-10 | RF-047 | Mantido |
| RE-11 | RF-005, RF-006, RF-021 | Dividido entre competências fixas, competências específicas e vínculo do feedback à competência |
| RE-12 | RF-007, RF-008 | Dividido entre questionários reutilizáveis e questionário padrão |
| RE-13 | RF-009 | Prioridade elevada para Should |
| RE-14 | RF-010 | Mantido |
| RE-15 | RF-042, RN-006 | Dividido entre plano de ação (RF) e definição conjunta (RN) |
| RE-16 | RF-043 | Unido a RA-18, RP-04, RP-07, RP-14 |
| RE-17 | RF-045 | Unido a RP-04 |
| RE-18 | RF-024, RF-027 | Dividido entre modalidades e resposta à avaliação |
| RE-19 | RF-025, RF-027 | Unido ao RA-11, que foi corrigido; apoia também a resposta à avaliação |
| RE-20 | RF-029 | Unido a RP-06 |
| RE-21 | RF-033 | Unido a RQ-18 |
| RE-22 | RF-034 | Unido a RP-08 |
| RE-23 | RF-017 | Unido a RQ-03, RD-37 e RA-21; prioridade elevada para Should |
| RE-24 | RF-048, RF-049 | Dividido entre histórico e painel |
| RE-25 | RF-044, RF-050 | Dividido entre acompanhamento de planos e painel do RH |
| RE-26 | RF-052 | Mantido |
| RE-27 | RF-003 | Unido a RD-14, RP-17 |
| RE-28 | RF-001, RF-002 | Dividido entre cadastro manual e importação |
| RE-29 | RNF-001 | Unido ao RQ-05 e RD-14, somando o gestor direto |
| RE-30 | RNF-013 | Ajustado para meta verificável |
| RE-31 | RN-001 | Unido a RD-44, RA-24 |
| RE-32 | RN-003 | Unido a RD-47 |
| RE-33 | RF-030, RN-004 | Unido aos modos de identificação do RD-15 |
| RE-34 | RN-007 | Unido a RD-46, RP-10 |
| RE-35 | RF-064, RN-009 | Unido ao RD-48, dividido entre regra (RN) e atalho para o canal (RF) |
| RE-36 | RF-062, RN-011 | Unido ao RD-24, dividido entre política configurável (RF) e prazo padrão (RN); prazo padrão de 5 anos, conforme a PO |
| RE-37 | RN-010 | Mantido; absorve o RD-23 |

### 11.2 Questionários

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RQ-01 | RF-022 | Unido a RE-06, RA-09 |
| RQ-02 | RF-005, RF-007 | Unido às competências e aos questionários |
| RQ-03 | RF-017 | Unido a RE-23, RD-37, RA-21, RP-03, RP-05, RP-09, RP-13 |
| RQ-04 | RN-004 | Unido aos modos de identificação; ascendente confidencial por padrão |
| RQ-05 | RNF-001 | Unido ao RE-29 e RD-14; a Diretoria vê só dados agregados |
| RQ-06 | RF-031 | Unido a RA-06 |
| RQ-07 | RF-042 | Unido a RE-15, RA-18, RP-14 |
| RQ-08 | RF-046, RN-006 | Unido ao RE-15 como RN; também origina as metas individuais (RF-046) |
| RQ-09 | RF-048 | Unido a RE-24, RD-47, RP-01, RP-10, RP-11 |
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
| RQ-21 | RF-040 | Unido ao RP-06 e RP-14; prioridade elevada para Should |

### 11.3 Pesquisa documental

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
| RD-09 | RF-020 | Unido a RP-13 |
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

### 11.4 Sistema análogo

| Candidato | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|
| RA-01 | RF-041 | Mantido; o gestor define a quem os check-ins se aplicam |
| RA-02 | RF-011 | Unido a RE-02, RP-01, RP-11 |
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
| RA-14 | RF-007 | Unido a RE-12, RQ-02, RP-02, RP-16 |
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

### 11.5 Processo AS-IS em BPMN

Os candidatos `RP` foram extraídos nesta consolidação (seção 2.1), por isso a tabela traz também a necessidade e o elemento do diagrama de onde cada um saiu. Os nomes dos elementos são os dos diagramas.

| Candidato | Necessidade | Diagrama · elemento · dor | Requisito(s) definitivo(s) | Tratamento |
|---|---|---|---|---|
| RP-01 | Registrar no sistema os fatos e os feedbacks, formais e informais, em vez de papel ou planilha | AS-IS 1 · Coletar fatos e fazer os check-ins; Coletar o fato e decidir dar o feedback; Registrar o feedback · D1 (E01 §6, §18) | RF-011, RF-013, RF-014, RF-048 | Unido a RE-01, RE-02, RE-04 e RE-24 |
| RP-02 | Diminuir o trabalho de planejar a avaliação de cada pessoa, reaproveitando questionários | AS-IS 1 · Planejar objetivos, competências e indicadores · D2 (E01 §9) | RF-007, RF-008 | Unido ao RE-12 |
| RP-03 | Preparar o receptor para receber o feedback de forma reflexiva, e não defensiva | AS-IS 1 · Receber o feedback e refletir · D3 (E01 §13, §20, §22) | RF-016, RF-017 | Unido a RE-03 e RE-23 |
| RP-04 | Registrar, na data final do plano de ação, se o colaborador melhorou | AS-IS 1 · decisão Melhorou até a data final? · D4 (E01 §6) | RF-043, RF-045 | Unido a RE-16 e RE-17 |
| RP-05 | Orientar o emissor a dar feedback com base em fatos, sem agressividade e sem deixar de elogiar | AS-IS 1 · Conduzir o feedback (positivo ou construtivo) · D5 (E01 §20) | RF-016, RF-017 | Unido a RE-03 e RE-23 |
| RP-06 | Mostrar quem não respondeu ao 360° e lembrar os avaliadores do prazo | AS-IS 1 · Avaliar o colega no 360º · D6 (E01 §21) | RF-029, RF-040 | Unido a RE-20 e RQ-21; elevou RF-040 para Should |
| RP-07 | Acompanhar o plano de ação nos check-ins | AS-IS 1 · Monitorar o plano nos check-ins · sem dor (E01 §4, §5) | RF-041, RF-043 | Unido a RE-06, RE-16 e RA-01 |
| RP-08 | Avaliar a sessão de feedback depois de registrá-la | AS-IS 1 · Registrar o feedback e avaliar a sessão · sem dor (E01 §13) | RF-034 | Unido ao RE-22 |
| RP-09 | Deixar disponível a quem dá e a quem recebe feedback o conteúdo do treinamento feito pelo RH | AS-IS 1 · Treinar quem dá e quem recebe feedback (raia RH) · sem dor (E01 §13) | RF-017 | Unido ao RE-23 |
| RP-10 | Permitir ao RH consultar o histórico de feedbacks quando houver decisão sobre a pessoa | AS-IS 1 · Consultar o histórico de feedbacks (raia RH) · sem dor (E01 §10) | RF-048, RF-051, RN-007 | Unido a RE-24, RE-34 e RD-47 |
| RP-11 | Registrar no sistema os fatos, os feedbacks e os elogios que hoje ficam de boca, no caderninho ou no WhatsApp | AS-IS 2 · Anotar no caderninho (nem sempre); Enviar o elogio por mensagem (WhatsApp) · D1 (E02 §2, §3, §4) | RF-011, RF-013, RF-015, RF-048 | Unido a RE-01, RE-02, RE-04 e RE-24 |
| RP-12 | Evitar que o feedback deixe de acontecer porque as agendas não coincidem | AS-IS 2 · decisão Há horário em comum? · D2 (E02 §2, §8) | RF-037, RF-038 | Unido a RE-08 e RE-09 |
| RP-13 | Dar ao receptor um meio de registrar sua posição sem que a conversa vire discussão | AS-IS 2 · Justificar e discordar (vira discussão) · D3 (E02 §2) | RF-017, RF-020 | Unido a RD-09 e RE-23 |
| RP-14 | Acompanhar o combinado de melhoria com prazo e lembrete, sem depender da memória | AS-IS 2 · Combinar a melhoria de forma verbal; Acompanhar de modo informal, pelas anotações · D4 (E02 §2, §4) | RF-040, RF-042, RF-043 | Unido a RE-15, RE-16 e RQ-21; elevou RF-040 para Should |
| RP-15 | Registrar o relato de um colega sem expor quem relatou | AS-IS 2 · Avisar a secretária e pedir que converse com a pessoa (raia Pares) · D5 (E02 §3) | RF-012 | Unido ao RE-05 |
| RP-16 | Avaliar com formulário e indicadores, e não só pela percepção | AS-IS 2 · Confirmar o fato por conta própria · D6 (E02 §5) | RF-007, RF-023 | Unido a RE-07 e RE-12 |
| RP-17 | Funcionar em organização sem RH próprio | AS-IS 2 · raia RH sem tarefas (anotação) · sem dor (E02 §1) | RF-003, RN-004 | Unido ao RE-27; originou a restrição ao RH avaliado em RN-004 (C-14) |

---

## 12. Limitações

- **Fontes pequenas.** São duas entrevistas e dois questionários. Falta a visão de alguém de RH, que aparece só pelo que a PO disse sobre o perfil.
- **BPMN feito a partir das entrevistas.** Os dois diagramas modelam o que foi dito nas entrevistas, e não uma observação direta do processo. O AS-IS 1 também mistura a prática atual com a prática ideal descrita pela PO (documento do BPMN, seção 7). Por isso o BPMN foi usado para localizar as dores no fluxo e conferir a cobertura, e não como evidência independente. O processo proposto (TO-BE), opcional na issue #44, não foi modelado.
- **Decisões do grupo sem confirmação da PO.** Em dez pontos as fontes não davam resposta definitiva (seção 9). O grupo decidiu cada um com justificativa nas fontes, e as decisões aguardam a validação da PO. Os requisitos afetados estão escritos de acordo com a decisão e só passam a Validado com a confirmação da PO.
- **Metas numéricas.** Os valores dos RNF de desempenho, disponibilidade, backup e do feedback informal em uma tela vêm da pesquisa documental ou desta consolidação, e não de pedido da PO (ponto P-10). Eles estão detalhados, com critério de aceitação e método de verificação, na [especificação suplementar](Especificacao_Suplementar.md) (#51).
- **Escopo amplo de propósito.** A PO pediu requisitos amplos e disse que a arquitetura pode ser reduzida, por exemplo só a gestor e colaborador (E01 §24). A redução será decidida na segunda etapa do trabalho, sem alterar esta lista.
