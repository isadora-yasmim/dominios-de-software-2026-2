# Síntese dos Requisitos das Entrevistas

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Técnica de elicitação:** Entrevista semiestruturada
**Issue:** #41 · **Data:** 17/11/2026
**Artefatos relacionados:** [Requisitos_Entrevistas.csv](Requisitos_Entrevistas.csv) (mesmas tabelas da seção 3, para a lista geral e a matriz de rastreabilidade)

**Fontes analisadas:**

| Código | Entrevistada | Função | Data | Duração | Transcrição |
|---|---|---|---|---|---|
| E01 | Adriana Silveira de Souza | Product Owner (professora da disciplina) | 20/10/2026 | 01:57:54 | [Entrevista01_Adriana.md](Entrevista01_Adriana.md) |
| E02 | Eliene de Souza Oliveira | Secretária Municipal de Educação (gestora de 23 servidores na secretaria) | 17/11/2026 | 00:18:00 | [Entrevista02_Eliene.md](Entrevista02_Eliene.md) |

> Os telefones das entrevistadas foram omitidos desta síntese (minimização de dados – LGPD).

---

## Sumário

1. [Objetivo e método](#1-objetivo-e-método)
2. [Principais achados](#2-principais-achados)
3. [Requisitos candidatos](#3-requisitos-candidatos)
4. [Resumo](#4-resumo)
5. [Pontos em aberto e tratamento na lista geral](#5-pontos-em-aberto-e-tratamento-na-lista-geral)
6. [Limitações](#6-limitações)

---

## 1. Objetivo e método

**Objetivo.** Extrair das duas entrevistas os requisitos funcionais (RF), não funcionais (RNF) e as regras de negócio (RN) do sistema, identificando a fonte de cada um.

**Método.**

1. As duas transcrições foram lidas por completo. Cada pedido, dor ou regra citada pelas entrevistadas foi anotado com a seção da transcrição em que aparece.
2. Pedidos sobre o mesmo assunto foram juntados em um único requisito candidato `RE-xx`, seguindo o padrão de identificação do [processo de requisitos](../../planejamento/Processo_Requisitos.md).
3. Cada requisito foi classificado como RF, RNF (com a característica da ISO/IEC 25010) ou RN, conforme as definições da seção 5.2 do processo.
4. A coluna **Relação com outras fontes** liga o requisito aos candidatos já levantados nos questionários (`RQ-xx`), na pesquisa documental (`RD-xx`) e no sistema análogo (`RA-xx`), para facilitar a lista geral (#45) e a matriz de rastreabilidade (#49).
5. A prioridade segue os critérios MoSCoW do processo de requisitos. Ela é uma proposta e será confirmada na lista geral.

**Legenda da coluna Fonte:** E01 = entrevista com a PO; E02 = entrevista com a secretária de educação; § = seção da transcrição.

**Perfis das fontes.** As duas entrevistas se complementam. A E01 traz a visão de quem conhece o processo de feedback e define o produto. A E02 mostra como o feedback acontece hoje em uma organização real, de forma totalmente informal e sem nenhuma ferramenta.

---

## 2. Principais achados

### 2.1 Pontos em comum

1. **A falta de registro é a dor central.** A PO diz que, no processo manual, a informação se perde e não se sabe se o colaborador melhorou (E01 §6, §18). A secretária diz que "tudo fica na memória" e que o único registro é um caderninho de anotações (E02 §2, §4).
2. **O feedback parte de fatos observados.** Para a PO, os fatos são campo obrigatório (E01 §2). A secretária também verifica por conta própria antes de conversar com a pessoa (E02 §4).
3. **O feedback construtivo termina em um combinado.** A PO chama de plano de ação, com pontos de monitoramento e data final (E01 §4). A secretária chama de "combinado de melhoria", acompanhado de forma informal (E02 §2, §4).
4. **O feedback positivo é menos frequente.** A PO cita isso como resultado de pesquisa (E01 §20). A secretária faz poucos elogios, geralmente por mensagem de WhatsApp (E02 §2).
5. **Achar um horário para a conversa é difícil.** A PO pede agendamento, comunicado e lembrete da sessão (E01 §5). Para a secretária, a agenda é a maior dificuldade, e foi a única coisa que ela pediu ao sistema (E02 §2, §8).
6. **O sistema não pode dar trabalho demais.** A PO diz que dar feedback "dá trabalho" e por isso costuma ser mal feito (E01 §9). A secretária diz que o sistema não deve fazê-la "ficar horas preenchendo informações" (E02 §8).
7. **A reação de quem recebe é um problema.** As duas citam o receptor que se defende ou se justifica, em vez de refletir (E01 §20; E02 §2).

### 2.2 Divergências

| Tema | E01 (PO) | E02 (secretária) |
|---|---|---|
| Quem vê o feedback | Receptor, emissor e RH. O RH vê inclusive quem emitiu (§11, §14) | Só a gestora e a pessoa (§6). A secretaria não tem RH próprio |
| Identificação do emissor | Transparência: o receptor sabe quem deu o feedback do gestor. Entre pares, a identidade pode ser omitida (§11) | Prefere anônimo entre equipes, porque "todo mundo se conhece" em cidade pequena (§6). Já protege quem reclama de um colega (§3) |
| Formal × informal | Formal é planejado, com objetivos, indicadores e check-ins. Informal é *ad hoc* (§5, §12) | "É tudo a mesma coisa"; a diferença é só marcar com antecedência (§3) |
| Indicadores | Todo objetivo amplo deve ter indicadores (§5, §29) | Não mede nada; avalia pela percepção (prazos, reclamações, documentos corretos) (§5) |

### 2.3 Restrições de escopo definidas pela PO

- O foco é o desenvolvimento da pessoa. O sistema não decide promoção nem salário (E01 §8).
- O sistema não é canal de denúncia (E01 §32).
- O sistema atende a uma organização específica (E01 §25, §31).
- Os requisitos podem ser amplos. Na arquitetura, o escopo pode ser reduzido, por exemplo só gestor e colaborador (E01 §24).

---

## 3. Requisitos candidatos

### 3.1 Requisitos funcionais

| ID | Requisito | Fonte | Evidência | Prioridade | Relação com outras fontes |
|---|---|---|---|---|---|
| RE-01 | O sistema deve permitir registrar um feedback com emissor, receptor, data, tipo (positivo ou construtivo), modalidade (formal ou informal), descrição e os fatos que o motivaram. | E01 §1, §2, §18; E02 §2, §3 | A PO lista os campos (E01 §2, §18). Hoje nada é registrado (E02 §2, §3) | Must | RA-24; RD-44 |
| RE-02 | O emissor deve poder registrar fatos e comportamentos observados ao longo do período, com data, e vinculá-los depois a um feedback. | E01 §1, §17; E02 §2, §4 | "Eu coleto fatos, registro os fatos, e depois eu posso linkar" (E01 §1). Anotações no caderninho (E02 §2, §4) | Must | RA-02; RD-44 |
| RE-03 | Ao escolher o tipo de feedback, o sistema deve apresentar a estrutura correspondente. Positivo: ação ou comportamento, resultados e repercussão para gestor, time e organização. Construtivo: aspecto positivo, fatos, problema, repercussão, reflexão e plano de ação. | E01 §3, §16 | A PO descreve as duas estruturas e aprova trazê-las prontas ao escolher a categoria (E01 §16) | Should | RQ-03; RA-21; RD-37 |
| RE-04 | O sistema deve permitir registrar um feedback informal a qualquer momento, sem planejamento prévio, inclusive um elogio rápido e um feedback para colaborador de outra área. | E01 §3, §10, §12; E02 §2, §4 | Informal é *ad hoc* (E01 §12). Gestor pode dar feedback a pessoa de outra área (E01 §10). Elogios hoje vão por WhatsApp (E02 §2, §4) | Must | RA-03 |
| RE-05 | O gestor deve poder registrar um fato relatado por outro colaborador, marcado como relato, sem expor ao receptor quem relatou. | E02 §3, §4, §6 | Colegas pedem que a gestora converse com alguém, e ela não revela quem reclamou (E02 §3, §6) | Could | Conflita com RE-31 (ver seção 5) |
| RE-06 | O sistema deve permitir planejar um ciclo de feedback formal, com período, objetivos (comportamentos ou resultados), competências, modalidades, participantes e datas dos check-ins de verificação, para um indivíduo ou para uma equipe. | E01 §5, §14, §17 | Periodicidade de 3 ou 4 meses, objetivos claros e check-ins mensais (E01 §5, §17). O planejamento define se é feedback do indivíduo ou da equipe (E01 §17) | Must | RQ-01; RA-09; RD-40 |
| RE-07 | Para cada objetivo, o sistema deve permitir definir indicadores e as fontes de evidência (por exemplo, avaliação do cliente ou do setor parceiro, pontualidade das entregas) e registrar os valores em cada check-in. | E01 §5, §14, §29 | "Melhorar a comunicação" precisa de indicador (E01 §5). Comprometimento medido por pontualidade e assiduidade (E01 §14) | Should | RA-16; RD-43 |
| RE-08 | O sistema deve permitir agendar a sessão de feedback (data, hora e participantes) e enviar aos participantes um comunicado e um lembrete. | E01 §5, §11; E02 §2, §8 | Pede "um comunicado de sessão" e um lembrete (E01 §5). A falta de horário é a maior dificuldade (E02 §2) | Should | RQ-21; RA-08 |
| RE-09 | Ao agendar uma sessão, o sistema deve sugerir horários em que o emissor e o receptor estejam livres. | E02 §2, §8 | Única coisa pedida ao sistema: "achar um momento em que eu e a pessoa estivéssemos livres" (E02 §8) | Could | — |
| RE-10 | O sistema deve permitir cadastrar metas por equipe para um período (por exemplo, bimestral), definidas pela própria equipe e pelo gestor. | E01 §9, §17; E02 §7 | Metas bimestrais por equipe, com autonomia das equipes (E02 §7). Planejamento por cargo ou grupo (E01 §9) | Should | RQ-08; RA-16 |
| RE-11 | O sistema deve permitir cadastrar competências fixas por cargo e competências específicas para um colaborador ou grupo. | E01 §9, §10 | Competências fixas do cargo, além de específicas para uma pessoa (E01 §9). O gestor é quem mais personaliza (E01 §10) | Must | RQ-02; RA-17 |
| RE-12 | O sistema deve permitir salvar parâmetros, indicadores e perguntas de avaliação para reutilizar em outros ciclos, incluindo um formulário padrão do RH com perguntas adicionais por pessoa. | E01 §15, §29 | A PO aprova manter uma lista de parâmetros reutilizáveis (E01 §15). Formulário pré-pronto do RH mais metas individuais (E01 §29) | Should | RQ-02; RA-14; RD-40 |
| RE-13 | O sistema deve permitir configurar a escala de cada pergunta ou indicador: ordinal, numérica ou atingido/não atingido. | E01 §27, §29 | A escala "pode ser ordinal, pode ser numérica"; o resultado não precisa ser binário (E01 §27) | Could | RD-40 |
| RE-14 | O sistema deve permitir atribuir pesos diferentes aos feedbacks e aos indicadores de um mesmo feedback. | E01 §37 | O feedback mais recente pode valer mais; pesos também entre indicadores (E01 §37) | Could | — |
| RE-15 | A partir de um feedback construtivo, o sistema deve permitir criar um plano de ação, construído em conjunto por emissor e receptor, com ações, metas, pontos de monitoramento e data final. | E01 §4; E02 §2, §4 | "Esse planejamento, ele é produto da colaboração dos dois" (E01 §4). A conversa termina com "um combinado de melhoria" (E02 §4) | Must | RQ-07; RQ-08; RA-18 |
| RE-16 | O sistema deve permitir acompanhar o plano de ação: registrar cada ponto de monitoramento, ajustar ações e, na data final, registrar se houve melhora ou se é necessário um novo feedback. | E01 §4, §6; E02 §4 | Sem registro "não tenho controle se houve uma melhora" (E01 §6). O acompanhamento hoje é por anotações (E02 §4) | Must | RQ-17; RA-18 |
| RE-17 | O sistema deve permitir consultar quais feedbacks e planos de ação geraram melhora. | E01 §4, §6 | "Quais são os feedbacks que tiveram um bom desempenho... seria interessante eu ter esse controle" (E01 §4) | Should | — |
| RE-18 | O sistema deve suportar as modalidades gestor → colaborador, colaborador → gestor, entre pares ou equipe, 360° e autoavaliação. O planejamento do ciclo define quais modalidades serão usadas. | E01 §12, §14, §17 | A PO confirma todas as modalidades, incluindo o autofeedback (E01 §12) | Must | RQ-04; RQ-15; RA-10 |
| RE-19 | Na avaliação 360°, o gestor deve abrir o ciclo e selecionar ou convidar os participantes do próprio time. | E01 §14, §21 | O gestor "pode abrir isso" e convidar os participantes do time (E01 §21). O 360° é só do time (E01 §14) | Should | RQ-15; RA-11 (conflito, ver seção 5) |
| RE-20 | O sistema deve registrar quem foi convidado para uma avaliação e não respondeu, e mostrar essa informação ao gestor e ao RH, sem aplicar nenhuma consequência automática. | E01 §21 | "A informação que eu tenho que saber é: tal pessoa não participou". Consequências estão fora do escopo (E01 §21) | Should | — |
| RE-21 | O sistema deve comparar a autoavaliação de uma pessoa com a avaliação feita pelos colegas, mostrando onde as percepções convergem ou divergem. | E01 §14 | Comparar "a minha percepção sobre a percepção dos meus colegas sobre mim" (E01 §14) | Should | RQ-18 |
| RE-22 | Após a sessão de feedback, o sistema deve permitir que o emissor avalie a postura do receptor (colaborativa ou reativa) e que o receptor avalie se o feedback agregou valor. | E01 §13; E02 §2 | Avaliar o processo para saber se ele está funcionando de forma adequada (E01 §13). Receptor que se justifica trava a conversa (E02 §2) | Should | — |
| RE-23 | O sistema deve oferecer orientações sobre como dar e como receber feedback. | E01 §13, §19, §22; E02 §2 | A PO começa todo processo com treinamento para quem dá e para quem recebe (E01 §13). Resistência ao receber (E02 §2) | Could | RQ-03; RD-37 |
| RE-24 | O sistema deve manter o histórico de feedbacks de cada colaborador e mostrar a evolução de cada indicador ao longo do tempo, em gráficos. | E01 §6, §15, §18; E02 §5, §7 | Trazer feedbacks anteriores para ver a evolução (E01 §15). Hoje não há histórico (E02 §7); "um sistema completo... ajudaria bastante" (E02 §5) | Must | RQ-09; RQ-10; RA-20; RD-43; RD-47 |
| RE-25 | O RH deve poder acompanhar os feedbacks e os planos de ação de toda a organização. | E01 §10 | "O RH tem que ter esse controle" dos feedbacks dados (E01 §10) | Should | RQ-17; RD-14 |
| RE-26 | O sistema deve permitir consultar problemas recorrentes de um cargo, mesmo depois que o ocupante saiu, para orientar quem assume o cargo. | E02 §6 | "Às vezes os problemas estão relacionados ao cargo em si, não à pessoa" (E02 §6) | Could | RD-24; RD-49 (ver seção 5) |
| RE-27 | O sistema deve ter os perfis colaborador, gestor, RH e administrador, com permissões diferentes. | E01 §10, §25 | RH como perfil (E01 §10). Cadastro feito pelo RH ou por um administrador (E01 §25) | Must | RD-14 |
| RE-28 | O RH ou o administrador deve poder cadastrar colaboradores, cargos, equipes e a hierarquia (em vários níveis) manualmente ou por importação de planilha. | E01 §25, §30; E02 §1 | "Se você puder importar, ótimo, mas, se não, você vai cadastrar manualmente" (E01 §30). Hierarquia em níveis: professor → diretor → secretária (E02 §1) | Must | RD-39 |

### 3.2 Requisitos não funcionais

| ID | Requisito | Característica (ISO/IEC 25010) | Fonte | Evidência | Prioridade | Relação com outras fontes |
|---|---|---|---|---|---|---|
| RE-29 | Um feedback só pode ser visto pelo receptor, pelo emissor e pelo RH. O RH pode ver a identidade do emissor e as autoavaliações. | Segurança (confidencialidade) | E01 §11, §14; E02 §6 | "O RH pode, ele tem autonomia para isso" (E01 §11). Na E02, só a gestora e a pessoa veem (E02 §6) | Must | RQ-05; RD-14; RD-22 |
| RE-30 | Registrar um feedback informal deve exigir poucos campos e poucos passos, para não tomar tempo da rotina do gestor. | Capacidade de interação (eficiência de uso) | E01 §9, §18; E02 §8 | "Essa atividade dá trabalho e por isso que muitas vezes ela é mal feita" (E01 §9). Não deve fazer a gestora "ficar horas preenchendo" (E02 §8) | Should | RQ-11 |

### 3.3 Regras de negócio

| ID | Regra | Fonte | Evidência | Prioridade | Relação com outras fontes |
|---|---|---|---|---|---|
| RE-31 | Todo feedback deve se basear em fatos ou comportamentos observados. Não pode tratar de características de personalidade nem de opiniões. | E01 §2, §11, §20; E02 §4 | Fatos são campo obrigatório, "porque você não entra muito no nível de subjetividade" (E01 §2). "Minha opinião não vale" (E01 §20) | Must | RD-44; RA-24 |
| RE-32 | Um feedback registrado não pode ser excluído, porque é registro oficial do histórico do colaborador. | E01 §20, §32 | "Deletar não dá... aquilo ali é uma informação oficial" (E01 §20). O histórico resguarda a organização juridicamente (E01 §32) | Must | RD-47; RA-13 |
| RE-33 | No feedback dado pelo gestor, o emissor é identificado para o receptor. Em feedbacks entre pares ou da equipe, a identidade do emissor pode ser omitida, conforme a configuração do ciclo. | E01 §11; E02 §3, §6 | "Ele sabe quem é o emissor... é uma coisa clara" (E01 §11). Entre pares, "talvez a gente possa omitir" (E01 §11). Anonimato evita conflito entre equipes (E02 §6) | Must | RQ-04; RQ-13; RD-15; RD-16; RA-12 |
| RE-34 | O sistema apoia o desenvolvimento das pessoas e não decide promoção, salário ou desligamento. O histórico pode ser usado pela organização como um dos critérios dessas decisões. | E01 §8, §10, §32 | "Eu focaria mais no desenvolvimento da pessoa" (E01 §8). Histórico como critério para promoção (E01 §10) | Must | RD-27; RD-46 |
| RE-35 | O sistema não é canal de denúncia. | E01 §32 | "Não é um software de reclamações, é um software de feedbacks"; "denúncia é denúncia" (E01 §32) | Must | RD-48 |
| RE-36 | Os feedbacks devem ser guardados enquanto o colaborador estiver na organização e por cerca de 5 anos depois que ele sair. | E01 §37; E02 §6 | Depois que a pessoa sair, "talvez cinco anos" (E01 §37). Guardar mesmo depois que a pessoa sai (E02 §6) | Should | RD-24 |
| RE-37 | Cada instalação do sistema atende a uma única organização. | E01 §25, §31 | "Uma ferramenta para ser usada por uma organização", na intranet ou como serviço para uma empresa (E01 §31) | Should | RD-23 |

---

## 4. Resumo

| Tipo | Must | Should | Could | Total |
|---|---|---|---|---|
| RF | 11 | 11 | 6 | 28 |
| RNF | 1 | 1 | — | 2 |
| RN | 5 | 2 | — | 7 |
| **Total** | **17** | **14** | **6** | **37** |

| Fonte | Requisitos | Total |
|---|---|---|
| E01 e E02 | RE-01, RE-02, RE-04, RE-08, RE-10, RE-15, RE-16, RE-22, RE-23, RE-24, RE-28, RE-29, RE-30, RE-31, RE-33, RE-36 | 16 |
| Somente E01 | RE-03, RE-06, RE-07, RE-11, RE-12, RE-13, RE-14, RE-17, RE-18, RE-19, RE-20, RE-21, RE-25, RE-27, RE-32, RE-34, RE-35, RE-37 | 18 |
| Somente E02 | RE-05, RE-09, RE-26 | 3 |

**Requisitos sem correspondência em outras fontes:** RE-05, RE-09, RE-14, RE-17, RE-20 e RE-22. Eles só aparecem nas entrevistas e devem ser conferidos com atenção na lista geral.

---

## 5. Pontos em aberto e tratamento na lista geral

Os pontos abaixo ficaram em aberto ao fim desta síntese. Todos foram decididos na consolidação da [lista geral](../../analise/Lista_Geral_Requisitos.md) (#45), como mostra a última coluna.

| # | Tema | O que as fontes dizem | Proposta | Tratamento na lista geral |
|---|---|---|---|---|
| 1 | RH vê todos os feedbacks? | A PO diz que sim, inclusive quem emitiu (E01 §11). Na E02, só a gestora e a pessoa veem (E02 §6) | Manter a visão da PO (RE-29), já que a E02 descreve uma organização sem RH próprio | Conflito C-03: união das listas da E01 e dos questionários (RNF-001) |
| 2 | Anonimato entre pares | A PO prefere transparência, mas aceita omitir o emissor entre pares (E01 §11). A E02 prefere anônimo (E02 §6). Se o RH vê o emissor, o modo é "confidencial", não "anônimo" (RD-15, RD-16) | Validar qual modo vale para pares e para a avaliação ascendente. A E02 diria a verdade ao superior mesmo identificada (E02 §6), ao contrário dos questionários (sinceridade 1,5/5) | Ponto P-01: confidencial como padrão, anônimo como opção por ciclo (RN-004, RF-030) |
| 3 | Relato de terceiros (RE-05) | A E02 recebe relatos de colegas (E02 §3). A PO exige fatos observados pelo emissor (RE-31) | Aceitar o relato só como fato registrado pelo gestor, marcado como relato, depois de ele verificar por conta própria (como a E02 já faz, §4) | Ponto P-06: relato marcado e confirmado pelo gestor (RF-012) |
| 4 | Edição de feedback | A PO só disse que não se pode excluir (E01 §20). A pesquisa documental pede versionamento das edições (RD-47) | Confirmar se a edição é permitida e se mantém a versão anterior | Ponto P-04: edição permitida, com versões (RN-003) |
| 5 | Uma ou várias organizações | A PO primeiro falou em várias empresas e depois em "uma empresa específica" (E01 §25, §31) | Confirmar RE-37 e se o sistema será instalado na intranet ou oferecido como serviço (RD-23, RD-25) | Conflito C-07: uma organização por instalação (RN-010) |
| 6 | Prazo de retenção | A PO disse "talvez cinco anos", sem norma definida (E01 §37) | Confirmar o prazo e o que acontece depois: eliminação ou anonimização (RD-24) | Ponto P-05: 5 anos, configurável; depois, eliminar ou anonimizar (RN-011, RF-062) |
| 7 | Sugestão de horários (RE-09) | Só a E02 pediu. Depende de o sistema conhecer a agenda dos usuários | Validar se entra no escopo ou se basta o agendamento com lembrete (RE-08) | Conflito C-12: sugestão de horários como Could (RF-038) |
| 8 | Problemas por cargo (RE-26) | A E02 quer consultar problemas do cargo depois que a pessoa sai | Mostrar só dados agregados e sem identificar o antigo ocupante (RD-49) | Ponto P-08: só dados agregados (RF-052) |
| 9 | Quem escolhe os avaliadores do 360° | A PO diz que é o gestor (E01 §21). O RA-11, na síntese do sistema análogo, diz que é o avaliado | Seguir a PO (RE-19) e corrigir o RA-11 na lista geral | Conflito C-01: o gestor escolhe os avaliadores (RF-025) |
| 10 | Escopo da arquitetura | A PO disse que a arquitetura pode se limitar a gestor e colaborador (E01 §24) | Usar essa informação ao priorizar as modalidades da RE-18 na lista geral | Seção 12 da lista geral (Limitações): a redução do escopo fica para a segunda etapa, sem alterar a lista |

---

## 6. Limitações

- **Só duas entrevistas**, com perfis muito diferentes: a PO, que conhece o processo ideal, e uma gestora do setor público de um município pequeno. Falta a visão de alguém de RH e de um colaborador sem cargo de gestão.
- **A E01 foi uma conversa coletiva** com a turma, guiada pelas perguntas de vários grupos, e não seguiu um roteiro. A transcrição é automática e tem trechos perdidos por falha de conexão (§2, §3, §20).
- **A E02 foi curta** (18 minutos) e descreve um processo totalmente informal. Ela ajuda a entender as dores atuais, mas não traz detalhes de avaliação formal. A avaliação de servidores (estágio probatório) segue regras de cada carreira, definidas fora da secretaria (E02 §2), e não foi tratada como requisito.
- **Os requisitos aqui são candidatos.** A prioridade final e a fusão com os requisitos das outras fontes serão feitas na lista geral (#45).
