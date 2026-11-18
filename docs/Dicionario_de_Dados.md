# Dicionário de Dados e Glossário

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software (INF0296, 2026/2) · 1ª Etapa: Levantamento de Requisitos
**Issue:** #53 · **Versão:** 1.1 · **Data:** 17/11/2026
**Responsável:** Ana Luísa Pereira dos Santos
**Referência de método:** Larman, *Utilizando UML e Padrões*, cap. 7 (Glossário e dicionário de dados)
**Base:** [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) (#45), versão 1.1, e [Modelo de Domínio e ER](modelagem/modelo-dados/Modelo_Dominio_ER.md) (#52), versão 1.1. Os identificadores `RF-`, `RNF-` e `RN-` são os da lista geral. Os `UC-` são os do [Diagrama de Casos de Uso](modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) (#47).

## Histórico de revisões

| Versão | Data | Descrição | Autora |
|---|---|---|---|
| 1.0 | 17/11/2026 | Versão inicial | Ana Luísa Pereira dos Santos |
| 1.1 | 17/11/2026 | Revisão final (#55): atributos e entidades conforme o modelo ER 1.1 (`DestinatarioVisibilidade`, `DisponibilidadeAgenda`, `TermoOfensivo`, `CheckInMeta`, `CheckInPlano` e atributos novos); perfis `DIRETORIA` e `ENCARREGADO`; inventário LGPD e prazos de retenção atualizados; coluna Tratamento na seção 5 | Verônica Ribeiro Oliveira Palmeira |

---

## Sumário

1. [Objetivo e método](#1-objetivo-e-método)
2. [Termos de negócio](#2-termos-de-negócio)
3. [Dicionário de atributos do modelo ER](#3-dicionário-de-atributos-do-modelo-er)
4. [Dados pessoais e sensíveis (LGPD)](#4-dados-pessoais-e-sensíveis-lgpd)
5. [Pontos não confirmados e inconsistências](#5-pontos-não-confirmados-e-inconsistências)
6. [Fontes](#6-fontes)

---

## 1. Objetivo e método

### 1.1 Objetivo

Dar um significado único a cada termo do domínio e descrever cada dado guardado pelo sistema. O documento completa a seção 2.4 da lista geral, que definiu alguns termos só para uso na própria lista e adiou o glossário para esta issue. Ele serve de apoio aos casos de uso completos (#48), à matriz de rastreabilidade (#49) e à especificação de requisitos.

### 1.2 Método

Larman (cap. 7) recomenda um glossário que funcione também como dicionário de dados. Para cada termo ou atributo, ele registra definição, sinônimos, formato (tipo, tamanho, unidade), relacionamentos e regras de validação. Este documento segue esse formato em três partes:

1. **Termos de negócio (seção 2).** Saem da lista geral, do Documento Visão, dos casos de uso, das sínteses de elicitação e do BPMN AS-IS. Cada termo aponta os requisitos que o usam.
2. **Atributos (seção 3).** Uma tabela por entidade do modelo ER, com os nomes exatamente como estão no ER. Nada foi renomeado.
3. **Dados pessoais (seção 4).** Classificação LGPD de cada atributo, com finalidade, base legal provável e prazo de retenção.

O documento **não cria requisitos**. Quando o ER não define um valor, como o tamanho de um texto, o valor proposto aqui fica marcado com `*` e é só uma sugestão para o projeto físico. Onde o ER e a lista geral divergem, a divergência está registrada na seção 5, e não corrigida aqui.

### 1.3 Como ler as tabelas da seção 3

| Coluna | Conteúdo |
|---|---|
| **Atributo** | Nome no modelo ER |
| **Definição** | O que o dado representa |
| **Tipo** | Tipo genérico do ER: `uuid`, `string`, `text`, `int`, `decimal`, `bool`, `date`, `datetime`, `enum` |
| **Tamanho ou domínio** | Tamanho máximo, faixa de valores ou enumeração |
| **Unid.** | Unidade de medida, quando houver |
| **Obr.** | Obrigatório: `sim` ou `não` |
| **Chave** | `PK` chave primária, `FK` chave estrangeira, `UK` valor único |
| **Relacionamento** | Entidade referenciada ou ligação relevante |
| **Regra de validação** | Restrição que o valor precisa cumprir, com o requisito de origem |
| **Dado pessoal** | Classificação da seção 4.1: `Não`, `Pessoal`, `Pessoal (R)` ou `Pessoal (C)` |

**Legenda.** `*` = **proposto**: o ER não define esse valor, e ele é uma sugestão deste documento. Valores sem `*` vêm do ER ou de um requisito citado na regra.

**Convenções de formato propostas** (valem para todas as tabelas, salvo indicação na linha):

| Tipo | Formato proposto | Observação |
|---|---|---|
| `uuid` | UUID versão 4, 36 caracteres na forma textual | Aleatório e não sequencial, para não revelar a ordem de inserção (ER, seção 10, item 3) |
| `date` | AAAA-MM-DD (ISO 8601) | Sem hora |
| `datetime` | AAAA-MM-DDThh:mm:ss, em UTC* (ISO 8601) | Exibido no fuso do usuário* |
| `decimal` | Até 10 dígitos, 2 casas decimais* | Pesos com 3 casas decimais* |
| `text` | Texto longo, com limite indicado na linha | Limites servem para manter o registro curto (RNF-013) e evitar abuso |
| `enum` | Um dos valores listados | Enumerações nomeadas na seção 11 do ER; as demais, na seção 3.7 deste documento |

---

## 2. Termos de negócio

Termos em ordem alfabética. A coluna **No modelo ER** indica onde o termo aparece no ER, para ligar o glossário ao dicionário de atributos.

| Termo | Definição | Sinônimos e termos a evitar | Relacionamento | No modelo ER | Origem |
|---|---|---|---|---|---|
| **Ação do plano** | Passo concreto de um plano de ação, com responsável, meta da ação e prazo | Sinônimo: ação de melhoria | Faz parte de um plano de ação. O responsável é um colaborador | `AcaoPlano` | RF-042, RF-043 |
| **Administrador** | Perfil de usuário que configura o sistema na organização: cadastros, parâmetros, finalidades e retenção dos dados. Não vê o conteúdo de feedbacks (Especificação Suplementar, seção 8.1) | Evitar "admin" nos documentos | É um perfil de usuário. Pode ser acumulado com outros perfis | `Perfil.ADMINISTRADOR` | RF-001, RF-002, RF-003, RF-054, RF-062, RNF-006, RNF-026 |
| **Anonimização** | Tratamento que impede associar um dado ao titular por meios técnicos razoáveis. O dado anonimizado deixa de ser dado pessoal (LGPD, art. 5º, III e XI, e art. 12) | Não confundir com pseudonimização | Uma das ações ao fim do prazo da política de retenção | `CategoriaDado.acao_fim_prazo`, `SituacaoColaborador.ANONIMIZADO` | RF-059, RF-062, RN-011, RN-015 |
| **Anônimo (modo)** | Modo de identificação em que ninguém, nem RH nem administrador, consegue ligar a resposta ao emissor | Evitar chamar de "anônimo" o modo confidencial. A palavra só aparece na interface quando o modo é este (Especificação Suplementar, seção 8.3) | É um modo de identificação. Exige o mínimo de respondentes na exibição | `ModoIdentificacao.ANONIMO`. Não gera `VinculoConfidencial` | RN-004, RN-005, RF-030 |
| **Autoavaliação** | Modalidade em que o colaborador avalia a si mesmo no ciclo. O resultado é comparado com a avaliação feita pelos demais avaliadores | Sinônimo: autofeedback (E01) | É uma modalidade. Quem responde é um avaliador convidado (o próprio avaliado) | `ModalidadeAvaliacao.AUTOAVALIACAO`, `DirecaoFeedback.AUTOAVALIACAO` | RF-024, RF-033 |
| **Avaliação** | Julgamento do desempenho feito com parâmetros definidos antes, em geral por questionário dentro de um ciclo. O feedback é a comunicação desse julgamento (E01 §14) | Não usar como sinônimo de feedback | Feita por um avaliador convidado, em uma modalidade do ciclo, com um questionário | `RespostaAvaliacao`, `ItemResposta` | RF-027, RF-028 |
| **Avaliação 360°** | Modalidade em que o gestor abre o ciclo e seleciona ou convida os participantes, que precisam ser do seu time | Escrever "360°" (símbolo de grau), como na lista geral. Evitar "360º" (ordinal) | É uma modalidade. Difere da avaliação de equipe, em que todos avaliam todos (ERS-D09; seção 5.3) | `ModalidadeAvaliacao.AVALIACAO_360` | RF-024, RF-025, RF-029 |
| **Avaliação ascendente** | Modalidade em que o colaborador avalia o seu gestor. O modo padrão é confidencial, e o ciclo pode ser configurado como anônimo | Sinônimo: colaborador → gestor | É uma modalidade. Protegida pelo mínimo de respondentes | `ModalidadeAvaliacao.ASCENDENTE`, `DirecaoFeedback.ASCENDENTE` | RF-024, RN-004, RN-005 |
| **Avaliação de equipe** | Modalidade em que todos os membros da equipe avaliam todos | Sinônimo: equipe (todos avaliam todos) | É uma modalidade. Ver a seção 5.3 | `ModalidadeAvaliacao.EQUIPE`, `DirecaoFeedback.EQUIPE` | RF-024, RN-004 |
| **Avaliado** | Colaborador que é objeto de avaliação em um ciclo, individualmente ou como membro de uma equipe | No ciclo, corresponde ao receptor | Participa de um ciclo. Recebe convites de avaliação e resultados consolidados | `AvaliadoCiclo.avaliado_id` | RF-022, RF-026 |
| **Avaliador convidado** | Papel de quem é convidado a responder uma avaliação de um ciclo: par, membro da equipe, liderado na avaliação ascendente ou o próprio avaliado na autoavaliação. É um papel, não um perfil | Sinônimos: participante convidado (RF-027), avaliador. Evitar "Par" como nome de ator (decisão do diagrama de casos de uso) | Recebe um convite de avaliação. É sempre um colaborador | `ConviteAvaliacao.avaliador_id`, `RespostaAvaliacao.avaliador_id` | RF-025, RF-027, RF-029 (UC-14) |
| **Base legal** | Hipótese da LGPD que autoriza o tratamento de um dado. Para feedback de empregados, a base principal é a execução de contrato ou o legítimo interesse. O consentimento fica restrito a funções opcionais | - | Definida por categoria de dado | `CategoriaDado.base_legal` (`BaseLegal`) | RF-054, RN-012 |
| **Cargo** | Função formal ocupada pelo colaborador. Define o conjunto de competências fixas | - | Ocupado por colaboradores. Exige competências | `Cargo` | RF-001, RF-005, RF-052 |
| **Check-in** | Encontro de verificação entre gestor e colaborador. No ciclo formal, registra os valores observados dos indicadores. No check-in periódico, acompanha metas e planos em andamento | Não confundir com ponto de monitoramento do plano (seção 5.3) | Pertence a um ciclo ou a uma configuração periódica. Colhe medições de indicadores | `CheckIn`, `ConfiguracaoCheckIn`, `MedicaoIndicador` | RF-022, RF-023, RF-036, RF-041 |
| **Ciclo de avaliação** | Período planejado de feedback formal, com avaliados, objetivos, competências, modalidades, questionários, participantes e datas dos check-ins | Sinônimos: ciclo, ciclo formal, ciclo de feedback formal (RF-022) | Combina modalidades, define objetivos e gera resultados consolidados | `CicloAvaliacao` | RF-022 a RF-026, RF-029, RF-032 |
| **Colaborador** | Pessoa da organização cadastrada no sistema. É também o perfil básico de todo usuário e o ator principal dos casos de uso | Sinônimos: servidor (E02), funcionário. Evitar "usuário" quando se fala da pessoa avaliada | Ocupa um cargo, integra uma equipe e tem um gestor direto | `Colaborador`, `Perfil.COLABORADOR` | RF-001, RF-003 |
| **Competência** | Conjunto de comportamentos observáveis esperado pela organização. Pode ser fixa (do cargo) ou específica (atribuída pelo gestor a um colaborador ou grupo) | - | Exigida por cargos, atribuída a colaboradores, avaliada por perguntas e tratada em feedbacks | `Competencia`, `CargoCompetencia`, `CompetenciaAtribuida` | RF-005, RF-006, RF-021, RN-001, RN-014 |
| **Confidencial (modo)** | Modo de identificação em que a identidade do emissor fica oculta para o receptor e guardada à parte. Só o RH consulta, com registro na trilha de auditoria, e nunca nas avaliações em que ele próprio é o avaliado. É o modo padrão entre pares, na equipe e na avaliação ascendente | Não chamar de "anônimo". Tecnicamente, é pseudonimização | É um modo de identificação | `ModoIdentificacao.CONFIDENCIAL`, `VinculoConfidencial` | RN-004, RNF-003, RNF-005, RF-030 |
| **Consentimento** | Manifestação livre, informada e inequívoca do titular para uma finalidade (LGPD, art. 5º, XII). Revogável a qualquer momento. Recusar não bloqueia o uso do sistema | - | Dado a um termo de consentimento. Só para funções opcionais | `TermoConsentimento`, `Consentimento` | RF-055, RN-012 |
| **Controlador** | Quem toma as decisões sobre o tratamento dos dados (LGPD, art. 5º, VI). Aqui, a organização que usa o sistema (Documento Visão, seção 5.3) | - | Indica o encarregado. Pode contratar um operador | `ConfiguracaoOrganizacao` (linha única da organização) | RF-054, RF-061, RF-063, RNF-034 |
| **Convite de avaliação** | Registro de que um avaliador foi chamado a avaliar um avaliado em uma modalidade do ciclo, com prazo e situação. Não tem ligação com a resposta | - | Gerado por uma modalidade do ciclo. Base para saber quem não respondeu | `ConviteAvaliacao` | RF-025, RF-027, RF-029, RNF-012 |
| **Dado pessoal** | Informação relacionada a pessoa natural identificada ou identificável (LGPD, art. 5º, I). O conteúdo de um feedback é dado pessoal de duas pessoas: de quem recebe e de quem emite (pesquisa documental, seção 3.1) | - | Ver a seção 4 | Coluna "Dado pessoal" da seção 3 | RNF-031, RN-013 |
| **Dado pessoal sensível** | Dado sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização religiosa, filosófica ou política, saúde, vida sexual, dado genético ou biométrico (LGPD, art. 5º, II) | - | O sistema não tem campos para esses dados. Textos livres podem contê-los por descuido | Nenhum atributo (RN-013) | RN-013, RN-015, RF-018 |
| **Diretoria** | Cúpula da organização. Vê apenas indicadores agregados, com o mínimo de respondentes | - | Usuário com perfil próprio e acesso restrito à sua função (RF-003) | `Perfil.DIRETORIA` | RF-003, RNF-001, RN-005 (P-02) |
| **Dor** | Problema do processo atual marcado no BPMN AS-IS (D1 a D6) | - | Origem de requisitos. Não é dado do sistema | - | Lista geral, seções 2.4 e 7.2 |
| **Emissor** | Quem dá o feedback ou responde a uma avaliação. A identidade dele segue o modo de identificação | Sinônimos: autor do feedback, avaliador (no ciclo) | Emite feedbacks e respostas. Com o receptor, define o plano de ação | `Feedback.emissor_id`, `RespostaAvaliacao.avaliador_id`, `VinculoConfidencial.emissor_id`, `PlanoAcao.emissor_id` | RF-013, RF-019, RN-002, RN-004 |
| **Encarregado** | Pessoa indicada pelo controlador para ser o canal de comunicação com os titulares e com a ANPD (LGPD, art. 5º, VIII, e art. 41). A identidade e o contato dele ficam no aviso de privacidade | Sinônimos: encarregado de dados, DPO (diagrama de casos de uso) | Trata solicitações de titulares e registra incidentes. Tem perfil próprio, com acesso restrito à sua função (RF-003) | `Perfil.ENCARREGADO`, `ConfiguracaoOrganizacao.encarregado_nome`, `encarregado_contato`, `SolicitacaoTitular.responsavel_id` | RF-003, RF-053, RF-061, RF-063 |
| **Equipe** | Grupo de colaboradores sob a responsabilidade de um gestor. Pode estar dentro de outra equipe | Sinônimos: time, setor (E02) | Pode ser receptora de feedback e ter metas | `Equipe` | RF-001, RF-013, RF-022, RF-047 |
| **Fato** | Comportamento ou resultado observado, com data e descrição, que fundamenta um feedback. Até ser vinculado a um feedback, é visível só para quem o registrou | Evitar "impressão", "opinião" e "achismo" (E01 §20) | Embasa feedbacks. Todo feedback tem ao menos um fato | `Fato`, `FeedbackFato` | RF-011, RF-018, RN-001, RN-002 |
| **Feedback** | Comunicação ao receptor sobre um comportamento ou resultado observado, baseada em fatos. Tem tipo (positivo ou construtivo) e é formal ou informal. Não pode ser excluído; cada edição gera uma versão | Não usar como sinônimo de avaliação | Tem emissor, receptor, fatos, competências e versões. Pode gerar plano de ação e sessão | `Feedback`, `VersaoFeedback` | RF-013, RN-001, RN-002, RN-003 |
| **Feedback construtivo** | Feedback que aponta um comportamento ou resultado a corrigir. Estrutura: aspecto positivo, fatos, problema, repercussão, reflexão e plano de ação | Evitar "feedback negativo" (E01 §22) | Pode originar um plano de ação | `TipoFeedback.CONSTRUTIVO` | RF-016, RF-042 |
| **Feedback em grupo** | Feedback cujo receptor é uma equipe. Aparece no histórico de cada membro da equipe na data do envio (decisão M-09 do ER) | - | Liga um feedback aos membros da equipe naquela data | `MembroFeedbackEquipe` | RF-013, RF-048 |
| **Feedback formal** | Feedback planejado dentro de um ciclo, com objetivos, indicadores e check-ins | - | Pertence a um ciclo | `Feedback.modalidade = FORMAL`, `Feedback.ciclo_id` | RF-013, RF-022 |
| **Feedback informal** | Feedback dado a qualquer momento, sem planejamento, inclusive para colaborador de outra área | Sinônimo: *ad hoc*. A grafia "a DOC" da transcrição (E01 §3) é erro de transcrição | Não pertence a ciclo | `Feedback.modalidade = INFORMAL` | RF-014, RF-015 |
| **Feedback positivo** | Feedback que reconhece uma ação ou comportamento com bons resultados. Estrutura: ação ou comportamento, resultados e repercussão para o gestor, o time e a organização | Sinônimos: reconhecimento, elogio | No modo informal, usa o formulário simplificado de RF-015 | `TipoFeedback.POSITIVO` | RF-015, RF-016 |
| **Gestor** | Perfil de quem tem uma equipe sob sua responsabilidade. Planeja ciclos, atribui competências específicas e configura check-ins. Também é avaliado, por isso acumula o perfil colaborador | Evitar "chefe" nos documentos | É um perfil de usuário. Gerencia equipes | `Perfil.GESTOR`, `Equipe.gestor_id` | RF-003, RF-006, RF-022, RF-025, RF-041 |
| **Gestor direto** | Gestor imediatamente acima do colaborador na hierarquia. É a base da regra de visibilidade | Sinônimo: chefe imediato | Liga dois colaboradores | `Colaborador.gestor_id` | RF-001, RNF-001 |
| **Histórico** | Conjunto, em ordem cronológica, dos feedbacks recebidos, avaliações, planos de ação e metas de um colaborador | - | Consulta sobre feedbacks, resultados, planos e metas. Não tem tabela própria (ER, seção 9) | Consulta | RF-048, RF-051, RN-003, RN-007 |
| **Identificado (modo)** | Modo de identificação em que o receptor vê quem emitiu. É obrigatório no feedback do gestor para o colaborador | - | É um modo de identificação | `ModoIdentificacao.IDENTIFICADO` | RN-004 |
| **Incidente de segurança** | Evento que compromete a segurança de dados pessoais. O registro guarda data, dados e titulares afetados e medidas adotadas, por no mínimo 5 anos | - | Afeta titulares | `IncidenteSeguranca`, `TitularAfetado` | RF-063 |
| **Indicador** | Medida que permite verificar se um objetivo do ciclo ou uma meta foi atingido, com fonte de evidência e valor esperado | - | Pertence a um objetivo do ciclo ou a uma meta. Recebe medições | `Indicador`, `MedicaoIndicador` | RF-023, RF-046, RF-049 |
| **Meta de desenvolvimento** | Resultado que o colaborador ou a equipe deve alcançar em um prazo, com competência, indicador e valor esperado. Definida em conjunto pelo colaborador e pelo gestor | Sinônimo: meta. Não confundir com a meta de uma ação do plano | Medida por indicadores | `Meta` | RF-046, RF-047, RN-006 |
| **Mínimo de respondentes** | Número mínimo de respostas de uma fonte confidencial ou anônima para que o resultado seja exibido. Padrão: 3 | - | Aplica-se aos resultados consolidados | `ConfiguracaoOrganizacao.min_respondentes`, `ModalidadeCiclo.min_respondentes` | RN-005 (P-03) |
| **Modalidade** | Quem avalia quem: gestor → colaborador, ascendente, pares, equipe, autoavaliação ou 360° (lista geral, seção 2.4) | Atenção: RF-013, RN-002 e `Feedback.modalidade` usam a palavra para "formal ou informal" (seção 5.3) | Um ciclo combina modalidades. Cada uma tem questionário e modo de identificação | `ModalidadeCiclo.modalidade` (`ModalidadeAvaliacao`), `Feedback.direcao` (`DirecaoFeedback`) | RF-024, RF-030 |
| **Modo de identificação** | Como a identidade do emissor é tratada: identificado, confidencial ou anônimo. Configurado pelo RH ou pelo administrador, por ciclo e por modalidade | - | Antes do envio, o emissor é informado de quem verá o conteúdo e a identidade (RF-019) | `ModoIdentificacao` | RN-004, RF-019, RF-030 |
| **Objetivo do ciclo** | Comportamento ou resultado que o avaliado deve atingir no ciclo | - | Medido por indicadores | `ObjetivoCiclo` | RF-022, RF-023 |
| **Operador** | Quem trata dados em nome do controlador (LGPD, art. 5º, VII). Aqui, o fornecedor do sistema quando ele é operado como serviço (pesquisa documental, seção 3.1) | - | Atua para o controlador | - | RNF-032, RNF-034 |
| **Par** | Colega que avalia outro colaborador ou dá feedback a ele, sem relação de gestão entre os dois. Em um ciclo, é um avaliador convidado | Sinônimos: colega, entre pares | É um papel, não um perfil | `ModalidadeAvaliacao.PARES`, `DirecaoFeedback.PARES` | RF-024, RN-004, RN-005 |
| **Perfil de usuário** | Conjunto de permissões de acesso: colaborador, gestor, RH, administrador, diretoria ou encarregado. Um usuário pode acumular perfis | Sinônimo: papel de acesso | Diretoria e encarregado têm acesso restrito à sua função (RF-003) | `PerfilColaborador`, `Perfil` | RF-003, RNF-001, RNF-006 |
| **Pergunta** | Item de um questionário, ligado ou não a uma competência e a um cargo, com tipo de resposta definido. O gestor pode acrescentar perguntas para um colaborador | - | Pertence a um questionário | `Pergunta` | RF-007, RF-008, RF-009, RN-001, RN-014 |
| **Plano de ação** | Conjunto de ações, responsáveis, metas, pontos de monitoramento e data final, criado a partir de um feedback construtivo, em conjunto pelo emissor e pelo receptor. Na data final, registra se houve melhora ou se é preciso novo feedback | - | Nasce de um feedback construtivo. Contém ações e pontos de monitoramento | `PlanoAcao`, `AcaoPlano`, `PontoMonitoramento` | RF-042 a RF-045, RN-006 |
| **Política de retenção** | Prazo de guarda de cada categoria de dado e ação ao fim do prazo (eliminar ou anonimizar). Padrão: enquanto o colaborador estiver na organização e por 5 anos depois do desligamento. Processo judicial em curso bloqueia a eliminação | Sinônimo: prazo de guarda | Aplicada pelo relógio do sistema | `CategoriaDado`, `BloqueioLegal`, `ConfiguracaoOrganizacao.retencao_pos_desligamento_meses` | RF-062, RN-011 (P-05) |
| **Ponto de monitoramento** | Data prevista do plano de ação em que se registra o resultado das ações | A lista geral (seção 2.4) chama isso também de check-in (seção 5.3) | Pertence a um plano de ação | `PontoMonitoramento` | RF-042, RF-043 |
| **Pseudonimização** | Tratamento após o qual o dado só pode ser associado ao titular com uma informação adicional guardada à parte (LGPD, art. 13, §4º). Continua sendo dado pessoal | Não confundir com anonimização | É a técnica do modo confidencial | `VinculoConfidencial` | RNF-003 |
| **Questionário** | Conjunto de perguntas usado em uma modalidade do ciclo ou em check-ins. Pode ser modelo reutilizável e padrão da organização | Sinônimo: formulário de avaliação | Contém perguntas. Usado por modalidades e por configurações de check-in | `Questionario` | RF-007, RF-008, RF-036 |
| **Receptor** | Quem recebe o feedback: um colaborador ou uma equipe | No ciclo, corresponde ao avaliado | Com o emissor, define o plano de ação. Pode registrar réplica | `Feedback.receptor_colaborador_id`, `Feedback.receptor_equipe_id`, `PlanoAcao.receptor_id` | RF-013, RF-020, RN-002 |
| **Relato** | Fato registrado pelo gestor a partir do que outro colaborador contou. Quem relatou fica oculto ao receptor. Só embasa um feedback depois de confirmado pela observação do próprio gestor | Evitar "denúncia" e "reclamação": o sistema não é canal de denúncia (RN-009) | É um tipo de fato | `Fato.eh_relato`, `Fato.relator_id`, `Fato.confirmado_pelo_autor` | RF-012 (P-06), RN-001, RN-009 |
| **Relógio do sistema** | Ator que representa o tempo e dispara tarefas automáticas: lembretes e política de retenção | - | Ator dos casos de uso UC-30 e UC-31. Não é usuário | `Notificacao.agendada_para` | RF-040, RF-062 |
| **Réplica** | Manifestação do receptor sobre um feedback recebido, sem alterar o texto do emissor | Sinônimo: manifestação | Ligada a um feedback | `Replica` | RF-020 |
| **Resultado consolidado** | Valor calculado ao encerrar o ciclo para cada avaliado, por competência, indicador e modalidade. Fica guardado e não muda depois de liberado (decisão M-08 do ER) | - | Respeita o mínimo de respondentes. Alimenta painéis e histórico | `ResultadoConsolidado` | RF-032, RF-033, RN-005, RN-008, RNF-007 |
| **RH** | Perfil da área de recursos humanos: cadastros, questionários padrão, modos de identificação, histórico e planos da organização. Pode consultar a identidade de emissores confidenciais, com auditoria. Em organização sem RH, um usuário recebe este perfil junto com o seu | - | É um perfil de usuário | `Perfil.RH` | RF-001, RF-003, RF-030, RF-051, RN-004 |
| **RIPD** | Relatório de Impacto à Proteção de Dados Pessoais: documento do controlador que descreve os tratamentos que podem gerar risco e as medidas para reduzi-lo (LGPD, art. 5º, XVII, e art. 38) | - | O sistema apoia com o inventário de dados (RF-054) e com a documentação técnica do fornecedor (RNF-034) | `CategoriaDado` | RF-054, RNF-034 |
| **Sessão de feedback** | Encontro agendado entre emissor, receptor e outros participantes para conversar sobre um feedback. O sistema agenda e registra, mas não conduz a conversa | - | Pode estar ligada a um feedback. Tem pauta compartilhada e anotações privadas | `SessaoFeedback`, `ParticipanteSessao` | RF-034, RF-037, RF-038, RF-039 |
| **Solicitação de feedback** | Pedido de um colaborador a colegas, fora do ciclo, com tema e prazo | - | Atendida por feedbacks | `SolicitacaoFeedback`, `DestinatarioSolicitacao` | RF-031 |
| **Solicitação de titular** | Pedido do titular para exercer um direito da LGPD, acompanhado em fila com prazo e responsável | Sinônimo: pedido de direito do titular | Tratada pelo RH ou pelo encarregado | `SolicitacaoTitular` | RF-056 a RF-061 |
| **Tipo de resposta** | Formato aceito por uma pergunta ou por um indicador: escala ordinal, valor numérico, atingido/não atingido ou texto livre | - | Definido na pergunta ou no indicador | `TipoResposta` | RF-009 |
| **Titular** | Pessoa natural a quem se referem os dados (LGPD, art. 5º, V). Aqui, colaboradores, gestores e demais avaliados ou avaliadores | - | Exerce direitos por solicitações de titular | `SolicitacaoTitular.titular_id`, `TitularAfetado.colaborador_id` | RF-053, RF-056 a RF-060 |
| **Trilha de auditoria** | Registro inalterável dos acessos e das alterações a dados pessoais e feedbacks: quem, quando, o quê e de onde. Inclui toda consulta à identidade de emissor confidencial | Sinônimo: log de auditoria | Somente inclusão, com encadeamento por hash | `RegistroAuditoria` | RNF-005, RNF-003, RF-035 |
| **Versão do feedback** | Cada estado do conteúdo de um feedback. Toda edição cria uma nova versão datada; a vigente é a de maior número | - | Pertence a um feedback | `VersaoFeedback` | RN-003 (P-04), RF-016 |
| **Visibilidade** | Quem pode ver um feedback. Por padrão, o público mínimo: receptor, emissor (só o que escreveu), gestor direto e RH. Só o emissor pode ampliá-la, por nova ação explícita | Termo do ER: "público mínimo" | Definida no envio do feedback | `Feedback.visibilidade` (`Visibilidade`) | RNF-001, RNF-002 |

---

## 3. Dicionário de atributos do modelo ER

Uma tabela por entidade, na ordem das seções 4 a 9 do [modelo ER](modelagem/modelo-dados/Modelo_Dominio_ER.md). Nomes de entidades e atributos sem alteração. Cada entidade traz uma linha com os **requisitos de origem**, com base na seção 12 e nas notas do ER. Lembre a legenda: `*` = proposto, porque o ER não define o valor.

### 3.1 Organização, usuários e acesso

#### `Colaborador`

Pessoa da organização cadastrada no sistema (RF-001). Guarda a hierarquia pelo autorrelacionamento `gestor_id`.

**Requisitos de origem:** RF-001, RF-048, RNF-001, RNF-006, RN-013, RN-016

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do colaborador | `uuid` | 36 | - | sim | PK | Referenciado pela maioria das entidades | Gerado pelo sistema | Pessoal |
| `matricula` | Matrícula na organização | `string` | 30* | - | sim* | UK | - | Única na organização | Pessoal |
| `nome` | Nome completo | `string` | 150* | - | sim* | - | - | Não pode ser vazio* | Pessoal |
| `email` | E-mail usado como login | `string` | 254* | - | sim* | UK | - | Formato de e-mail válido*. Único | Pessoal |
| `senha_hash` | Resumo criptográfico da senha | `string` | 255* | - | sim* | - | - | A senha nunca é guardada em claro. Usar algoritmo próprio para senhas, com sal* (RNF-004) | Pessoal |
| `dois_fatores_ativo` | Indica se a autenticação em dois fatores está ativa | `bool` | verdadeiro ou falso | - | sim | - | `PerfilColaborador` | Deve ser verdadeiro para quem tem perfil `RH` ou `ADMINISTRADOR` (RNF-006) | Não |
| `falhas_login_consecutivas` | Tentativas de login sem sucesso seguidas | `int` | 0 a 100 | tentativas | sim | - | - | Volta a zero no login com sucesso. Em 100 falhas seguidas, o autenticador é desativado (RNF-006, DS-06) | Não |
| `login_bloqueado_ate` | Fim da espera imposta após uma falha de login | `datetime` | data e hora | - | não | - | - | Espera crescente de 30 s até 1 h a cada falha (RNF-006, DS-06) | Não |
| `data_nascimento` | Data de nascimento | `date` | data passada | - | sim* | - | - | Usada só para calcular se o colaborador é menor de 18 anos, sem atributo próprio (RN-016, decisão M-07) | Pessoal |
| `data_admissao` | Data de entrada na organização | `date` | data | - | sim* | - | - | Menor ou igual a `data_desligamento`, quando houver* | Pessoal |
| `data_desligamento` | Data de saída da organização | `date` | data | - | não | - | `CategoriaDado` | Maior ou igual a `data_admissao`*. Preenchida quando `situacao = DESLIGADO`*. Inicia a contagem do prazo de retenção (RN-011) | Pessoal |
| `situacao` | Situação do vínculo | `enum` | `SituacaoColaborador`: `ATIVO`, `AFASTADO`, `DESLIGADO`, `ANONIMIZADO` | - | sim | - | - | `ANONIMIZADO` só pela política de retenção ou por pedido do titular* (RF-059, RF-062) | Pessoal |
| `cargo_id` | Cargo ocupado | `uuid` | 36 | - | sim | FK | `Cargo` | Cargo ativo* | Pessoal |
| `equipe_id` | Equipe que o colaborador integra | `uuid` | 36 | - | sim | FK | `Equipe` | Equipe ativa* | Pessoal |
| `gestor_id` | Gestor direto | `uuid` | 36 | - | não | FK | `Colaborador` (autorrelacionamento) | Nulo indica o topo da hierarquia. Não pode ser o próprio colaborador nem formar ciclo na hierarquia* (RF-001, RNF-001) | Pessoal |

#### `PerfilColaborador`

Perfis de acesso de cada colaborador. Um colaborador pode acumular perfis (RF-003, decisão M-01).

**Requisitos de origem:** RF-003, RNF-001, RNF-006

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `colaborador_id` | Colaborador que tem o perfil | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | Todo colaborador tem ao menos o perfil `COLABORADOR` (ER, seção 4) | Pessoal |
| `perfil` | Perfil concedido | `enum` | `Perfil`: `COLABORADOR`, `GESTOR`, `RH`, `ADMINISTRADOR`, `DIRETORIA`, `ENCARREGADO` | - | sim | PK | - | Perfis `RH` e `ADMINISTRADOR` exigem dois fatores (RNF-006). `DIRETORIA` vê só resultados agregados (RNF-001, RN-005). `ENCARREGADO` acessa as solicitações de titulares e os incidentes (RF-061, RF-063) | Pessoal |
| `concedido_em` | Data da concessão | `date` | data | - | sim* | - | - | Não futura* | Pessoal |

#### `Cargo`

Função formal ocupada pelo colaborador (RF-001).

**Requisitos de origem:** RF-001, RF-048, RNF-001

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do cargo | `uuid` | 36 | - | sim | PK | `Colaborador`, `CargoCompetencia`, `Pergunta` | Gerado pelo sistema | Não |
| `nome` | Nome do cargo | `string` | 100* | - | sim | UK | - | Único | Não |
| `descricao` | Descrição das atribuições | `text` | 2.000* caracteres | - | não* | - | - | - | Não |
| `ativo` | Indica se o cargo pode receber colaboradores | `bool` | verdadeiro ou falso | - | sim | - | - | Cargo inativo não recebe novos colaboradores* | Não |

#### `Equipe`

Grupo de colaboradores sob um gestor. Pode estar dentro de outra equipe (RF-001).

**Requisitos de origem:** RF-001, RF-048, RNF-001

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da equipe | `uuid` | 36 | - | sim | PK | `Colaborador`, `Feedback`, `Meta`, `AvaliadoCiclo` | Gerado pelo sistema | Não |
| `nome` | Nome da equipe | `string` | 100* | - | sim | - | - | Único dentro da mesma equipe superior* | Não |
| `gestor_id` | Gestor responsável pela equipe | `uuid` | 36 | - | sim | FK | `Colaborador` | Colaborador com perfil `GESTOR`* | Pessoal |
| `equipe_superior_id` | Equipe que agrupa esta | `uuid` | 36 | - | não | FK | `Equipe` (autorrelacionamento) | Não pode formar ciclo* | Não |
| `ativa` | Indica se a equipe está em uso | `bool` | verdadeiro ou falso | - | sim | - | - | - | Não |

#### `ImportacaoCadastro`

Registro de cada importação de cadastro por planilha (RF-002).

**Requisitos de origem:** RF-002

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da importação | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `executada_por` | Quem executou a importação | `uuid` | 36 | - | sim | FK | `Colaborador` | Colaborador com perfil `RH` ou `ADMINISTRADOR` (RF-001, RF-002) | Pessoal |
| `data_hora` | Momento da importação | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |
| `arquivo` | Nome do arquivo importado | `string` | 255* | - | sim | - | - | Arquivo CSV (RF-002) | Não |
| `linhas_importadas` | Linhas gravadas com sucesso | `int` | 0 ou mais | linhas | sim | - | - | Maior ou igual a zero | Não |
| `linhas_com_erro` | Linhas rejeitadas | `int` | 0 ou mais | linhas | sim | - | - | Maior ou igual a zero | Não |
| `log_erros` | Descrição dos erros encontrados | `text` | sem limite* (gerado pelo sistema) | - | não | - | - | Preenchido quando `linhas_com_erro` for maior que zero* | Pessoal |

#### `ConfiguracaoOrganizacao`

Configurações gerais. Tem uma única linha, porque cada instalação atende uma organização (RN-010, decisão M-06).

**Requisitos de origem:** RN-005, RN-010, RN-011, RF-053, RF-064, RF-065

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da linha única | `int` | sempre 1* | - | sim | PK | - | Só existe uma linha (RN-010) | Não |
| `nome_organizacao` | Nome da organização | `string` | 150* | - | sim* | - | - | - | Não |
| `min_respondentes` | Mínimo de respondentes para exibir resultado de fonte confidencial ou anônima | `int` | inteiro maior ou igual a 3; padrão 3 | respostas | sim | - | `ModalidadeCiclo.min_respondentes` | Padrão 3, configurável, nunca menor que 3 (RN-005) | Não |
| `retencao_pos_desligamento_meses` | Prazo de guarda após o desligamento | `int` | inteiro positivo; padrão 60 | meses | sim | - | `CategoriaDado.prazo_retencao_meses` | Padrão 60 meses (5 anos), configurável (RN-011). Vale para feedbacks, avaliações e planos quando a categoria não define prazo próprio. O prazo de `CategoriaDado` prevalece (RF-062) | Não |
| `aviso_privacidade` | Texto do aviso de privacidade | `text` | 20.000* caracteres | - | sim | - | - | Deve trazer finalidades, bases legais, compartilhamentos, prazos de retenção, direitos do titular e identidade e contato do encarregado (RF-053) | Não |
| `encarregado_nome` | Nome do encarregado de dados | `string` | 150* | - | sim | - | - | Exibido no aviso de privacidade (RF-053) | Pessoal |
| `encarregado_contato` | Contato do encarregado | `string` | 254* | - | sim | - | - | E-mail ou telefone válido* (RF-053) | Pessoal |
| `url_canal_denuncia` | Endereço do canal de denúncias da organização | `string` | 2.048* | - | não* | - | - | URL válida, com `https`* (RF-064) | Não |
| `declaracao_acessibilidade` | Texto da declaração de acessibilidade | `text` | 20.000* caracteres | - | sim | - | - | Deve trazer o nível de conformidade e um canal para reportar barreiras (RF-065) | Não |

### 3.2 Competências e questionários

#### `Competencia`

Comportamentos observáveis esperados pela organização (RF-005).

**Requisitos de origem:** RF-005, RF-006, RN-014

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da competência | `uuid` | 36 | - | sim | PK | `CargoCompetencia`, `CompetenciaAtribuida`, `Pergunta`, `FeedbackCompetencia`, `Meta` | Gerado pelo sistema | Não |
| `nome` | Nome da competência | `string` | 100* | - | sim | UK | - | Único | Não |
| `descricao` | Comportamentos observáveis que a definem | `text` | 2.000* caracteres | - | sim* | - | - | Sem traços de personalidade nem critério discriminatório (RN-001, RN-014). Verificado na revisão, não pelo esquema (ER, seção 5) | Não |
| `ativa` | Indica se a competência está em uso | `bool` | verdadeiro ou falso | - | sim | - | - | - | Não |

#### `CargoCompetencia`

Competências fixas de cada cargo (RF-005).

**Requisitos de origem:** RF-005, RF-010

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `cargo_id` | Cargo | `uuid` | 36 | - | sim | PK, FK | `Cargo` | - | Não |
| `competencia_id` | Competência exigida | `uuid` | 36 | - | sim | PK, FK | `Competencia` | Competência ativa* | Não |
| `peso` | Peso da competência no cargo | `decimal` | 0 ou mais*, 3 casas* | - | não | - | - | Maior ou igual a zero*. Peso de projeto, além do RF-010, exibido junto com o resultado (RN-008; I-06) | Não |

#### `CompetenciaAtribuida`

Competência específica atribuída pelo gestor a um colaborador, além das fixas do cargo (RF-006). A atribuição a um grupo gera uma linha por membro.

**Requisitos de origem:** RF-006

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da atribuição | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `colaborador_id` | Colaborador que recebe a competência | `uuid` | 36 | - | sim | FK | `Colaborador` | Membro da equipe de quem atribui* | Pessoal |
| `competencia_id` | Competência atribuída | `uuid` | 36 | - | sim | FK | `Competencia` | Competência ativa* | Não |
| `atribuida_por` | Gestor que atribuiu | `uuid` | 36 | - | sim | FK | `Colaborador` | Colaborador com perfil `GESTOR` (RF-006) | Pessoal |
| `data_inicio` | Início da vigência | `date` | data | - | sim* | - | - | - | Não |
| `data_fim` | Fim da vigência | `date` | data | - | não | - | - | Maior ou igual a `data_inicio`* | Não |
| `justificativa` | Motivo da atribuição | `text` | 1.000* caracteres | - | não | - | - | Orientação do RF-018 sobre dados sensíveis* | Pessoal (R) |

#### `Questionario`

Conjunto de perguntas reutilizável (RF-007, RF-008).

**Requisitos de origem:** RF-007, RF-008, RNF-026

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do questionário | `uuid` | 36 | - | sim | PK | `Pergunta`, `ModalidadeCiclo`, `ConfiguracaoCheckIn` | Gerado pelo sistema | Não |
| `titulo` | Título | `string` | 150* | - | sim | - | - | - | Não |
| `descricao` | Descrição e orientações | `text` | 2.000* caracteres | - | não | - | - | - | Não |
| `eh_modelo` | Indica se é modelo reutilizável em outros ciclos | `bool` | verdadeiro ou falso | - | sim | - | - | (RF-007) | Não |
| `eh_padrao_organizacao` | Indica se é o questionário padrão da organização | `bool` | verdadeiro ou falso | - | sim | - | - | Só o RH define (RF-008). No máximo um padrão vigente* | Não |
| `versao` | Número da versão | `int` | 1 ou mais | - | sim | - | - | Maior ou igual a 1* | Não |
| `questionario_origem_id` | Modelo do qual este é cópia | `uuid` | 36 | - | não | FK | `Questionario` (autorrelacionamento) | - | Não |
| `criado_por` | Quem criou | `uuid` | 36 | - | sim | FK | `Colaborador` | Perfil `RH`, `GESTOR` ou `ADMINISTRADOR`* (RF-008, RNF-026) | Pessoal |
| `criado_em` | Momento da criação | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `Pergunta`

Item de um questionário (RF-007 a RF-009).

**Requisitos de origem:** RF-007, RF-008, RF-009, RF-010, RN-001, RN-014

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da pergunta | `uuid` | 36 | - | sim | PK | `ItemResposta` | Gerado pelo sistema | Não |
| `questionario_id` | Questionário a que pertence | `uuid` | 36 | - | sim | FK | `Questionario` | - | Não |
| `competencia_id` | Competência avaliada | `uuid` | 36 | - | não | FK | `Competencia` | - | Não |
| `cargo_id` | Cargo a que a pergunta se restringe | `uuid` | 36 | - | não | FK | `Cargo` | - | Não |
| `colaborador_alvo_id` | Colaborador para quem o gestor acrescentou a pergunta | `uuid` | 36 | - | não | FK | `Colaborador` | Só o gestor do colaborador acrescenta* (RF-008) | Pessoal |
| `enunciado` | Texto da pergunta | `text` | 1.000* caracteres | - | sim | - | - | Não pode tratar de personalidade, vida privada ou critério discriminatório (RN-001, RN-014) | Não |
| `tipo_resposta` | Formato da resposta | `enum` | `TipoResposta`: `ESCALA_ORDINAL`, `NUMERICO`, `ATINGIDO_NAO_ATINGIDO`, `TEXTO_LIVRE` | - | sim | - | - | (RF-009) | Não |
| `escala_min` | Menor valor da escala | `int` | inteiro* | - | não | - | - | Obrigatório quando `tipo_resposta = ESCALA_ORDINAL`*. Menor que `escala_max` | Não |
| `escala_max` | Maior valor da escala | `int` | inteiro* | - | não | - | - | Obrigatório quando `tipo_resposta = ESCALA_ORDINAL`*. Maior que `escala_min` | Não |
| `peso` | Peso da pergunta no resultado | `decimal` | 0 ou mais*, 3 casas* | - | não | - | - | Maior ou igual a zero* (RF-010) | Não |
| `ordem` | Posição no questionário | `int` | 1 ou mais | - | sim* | - | - | Única dentro do questionário* | Não |
| `obrigatoria` | Indica se a resposta é obrigatória | `bool` | verdadeiro ou falso | - | sim | - | - | - | Não |

### 3.3 Fatos, feedbacks e sessões

#### `Fato`

Comportamento ou resultado observado, que fundamenta um feedback (RF-011, RF-012).

**Requisitos de origem:** RF-011, RF-012, RN-001

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do fato | `uuid` | 36 | - | sim | PK | `FeedbackFato` | Gerado pelo sistema | Não |
| `autor_id` | Quem registrou | `uuid` | 36 | - | sim | FK | `Colaborador` | Enquanto não houver vínculo em `FeedbackFato`, só o autor vê o fato (RF-011) | Pessoal |
| `observado_id` | Colaborador observado | `uuid` | 36 | - | não | FK | `Colaborador` | Exatamente um entre este e `observado_equipe_id` | Pessoal |
| `observado_equipe_id` | Equipe observada como um todo | `uuid` | 36 | - | não | FK | `Equipe` | Exatamente um entre este e `observado_id`. Só embasa feedback para a equipe (RN-001, decisão UC08-D02) | Não |
| `data_ocorrencia` | Data em que o fato ocorreu | `date` | data | - | sim | - | - | Não futura* (RF-011) | Pessoal |
| `descricao` | Descrição do fato | `text` | 2.000* caracteres | - | sim | - | - | Fato ou comportamento observável, sem personalidade nem vida privada (RN-001). Orientação contra dados sensíveis (RF-018) | Pessoal (R) |
| `eh_relato` | Indica se o fato veio do relato de outro colaborador | `bool` | verdadeiro ou falso | - | sim | - | - | Verdadeiro só se o autor tem perfil `GESTOR` (RF-012) | Não |
| `relator_id` | Colaborador que relatou | `uuid` | 36 | - | não | FK | `Colaborador` | Obrigatório quando `eh_relato` é verdadeiro*. Nunca exibido ao receptor (RF-012) | Pessoal (C) |
| `confirmado_pelo_autor` | Indica se o gestor confirmou o relato por observação própria | `bool` | verdadeiro ou falso; padrão falso* | - | sim | - | - | Um relato só pode ser vinculado a feedback se este campo for verdadeiro (RF-012) | Não |
| `registrado_em` | Momento do registro | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `Feedback`

Cabeçalho do feedback. O conteúdo fica em `VersaoFeedback` (RN-003).

**Requisitos de origem:** RF-010, RF-013, RF-014, RF-015, RF-021, RF-034, RN-002, RN-004, RNF-002

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do feedback | `uuid` | 36 | - | sim | PK | `VersaoFeedback`, `FeedbackFato`, `Replica`, `PlanoAcao`, `SessaoFeedback` | Gerado pelo sistema | Não |
| `emissor_id` | Quem deu o feedback | `uuid` | 36 | - | não | FK | `Colaborador` | Obrigatório no modo `IDENTIFICADO` e enquanto o feedback é rascunho. No modo `CONFIDENCIAL`, fica nulo após o envio, e a identidade vai para `VinculoConfidencial` (RN-002, RN-004, RNF-003) | Pessoal |
| `receptor_colaborador_id` | Colaborador que recebe | `uuid` | 36 | - | não | FK | `Colaborador` | Exatamente um entre este e `receptor_equipe_id` (ER, seção 6) | Pessoal |
| `receptor_equipe_id` | Equipe que recebe | `uuid` | 36 | - | não | FK | `Equipe` | Exatamente um entre este e `receptor_colaborador_id`. Gera `MembroFeedbackEquipe` | Não |
| `tipo` | Tipo do feedback | `enum` | `TipoFeedback`: `POSITIVO`, `CONSTRUTIVO` | - | sim | - | - | Obrigatório (RN-002). Define a estrutura de `VersaoFeedback` (RF-016) | Pessoal |
| `modalidade` | Formal ou informal | `enum` | `FORMAL`, `INFORMAL` | - | sim | - | - | Obrigatório (RN-002). Ver o termo "Modalidade" na seção 5.3 | Não |
| `direcao` | Quem avalia quem | `enum` | `DirecaoFeedback`: `GESTOR_COLABORADOR`, `ASCENDENTE`, `PARES`, `EQUIPE`, `AUTOAVALIACAO`, `OUTRA_AREA` | - | sim* | - | - | `GESTOR_COLABORADOR` e `OUTRA_AREA` usam o modo `IDENTIFICADO` (RN-004, ERS-D06) | Não |
| `peso` | Peso do feedback no cálculo dos resultados do período | `decimal` | 0 ou mais*, 3 casas* | - | não | - | - | Maior ou igual a zero* (RF-010). Exibido junto com o resultado calculado (RN-008) | Não |
| `modo_identificacao` | Modo de identificação do emissor | `enum` | `ModoIdentificacao`: `IDENTIFICADO`, `CONFIDENCIAL`, `ANONIMO` | - | sim | - | - | Segue a configuração da modalidade e a RN-004. O emissor vê o efeito antes do envio (RF-019). `ANONIMO` não é aceito em feedback: o anonimato só existe nas respostas de avaliação (ERS-D03) | Não |
| `visibilidade` | Quem pode ver | `enum` | `Visibilidade`: `PUBLICO_MINIMO`, `AMPLIADA` | - | sim | - | - | Padrão `PUBLICO_MINIMO`. Só o emissor amplia, por nova ação explícita (RNF-001, RNF-002) | Não |
| `ciclo_id` | Ciclo do feedback formal | `uuid` | 36 | - | não | FK | `CicloAvaliacao` | Obrigatório se `modalidade = FORMAL`* e nulo se `INFORMAL` (ER: "só feedback formal") | Não |
| `solicitacao_id` | Solicitação que o feedback atende | `uuid` | 36 | - | não | FK | `SolicitacaoFeedback` | O emissor deve ser destinatário da solicitação* (RF-031) | Não |
| `data_feedback` | Data do feedback | `date` | data | - | sim | - | - | Obrigatório (RN-002) | Não |
| `postura_receptor` | Postura do receptor na sessão, na avaliação do emissor | `enum` | `PosturaReceptor`: `COLABORATIVA`, `REATIVA` | - | não | - | - | Preenchido só pelo emissor, após a sessão (RF-034) | Pessoal |
| `agregou_valor` | Avaliação do receptor sobre o feedback | `bool` | verdadeiro ou falso | - | não | - | - | Preenchido só pelo receptor, após a sessão (RF-034) | Pessoal |
| `status` | Situação do registro | `enum` | `RASCUNHO`, `ENVIADO` | - | sim | - | - | Rascunho visível só ao autor (Especificação Suplementar, seção 8.1). Para enviar, precisa de ao menos um fato (RN-002). Depois de enviado, não pode ser excluído (RN-003) | Não |
| `enviado_em` | Momento do envio | `datetime` | data e hora | - | não | - | - | Obrigatório quando `status = ENVIADO`* | Não |

#### `VersaoFeedback`

Conteúdo do feedback. Cada edição cria uma versão; a vigente é a de maior `numero` (RN-003, decisão M-03).

**Requisitos de origem:** RF-016, RN-003

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da versão | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `feedback_id` | Feedback | `uuid` | 36 | - | sim | FK | `Feedback` | - | Não |
| `numero` | Número sequencial da versão | `int` | 1, 2, 3... | - | sim | - | - | Único por feedback* e crescente. Nenhuma versão é apagada (RN-003) | Não |
| `descricao` | Descrição geral | `text` | 4.000* caracteres | - | sim* | - | - | Baseada em fatos (RN-001). Orientação do RF-018 | Pessoal (R) |
| `acao_comportamento` | Ação ou comportamento reconhecido | `text` | 2.000* caracteres | - | não | - | - | Exigido no tipo `POSITIVO`*, salvo no formulário simplificado (RF-015, RF-016) | Pessoal (R) |
| `resultados` | Resultados da ação | `text` | 2.000* caracteres | - | não | - | - | Exigido no tipo `POSITIVO`*, salvo no formulário simplificado (RF-016) | Pessoal (R) |
| `repercussao` | Repercussão para o gestor, o time e a organização | `text` | 2.000* caracteres | - | não | - | - | Usado nos dois tipos (RF-016) | Pessoal (R) |
| `aspecto_positivo` | Aspecto positivo que abre o feedback construtivo | `text` | 2.000* caracteres | - | não | - | - | Exigido no tipo `CONSTRUTIVO`* (RF-016) | Pessoal (R) |
| `problema` | Problema associado aos fatos | `text` | 2.000* caracteres | - | não | - | - | Exigido no tipo `CONSTRUTIVO`* (RF-016) | Pessoal (R) |
| `reflexao` | Reflexão conduzida com o receptor | `text` | 2.000* caracteres | - | não | - | - | Usado no tipo `CONSTRUTIVO` (RF-016) | Pessoal (R) |
| `criada_em` | Momento da versão | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema. Torna cada versão datada (RN-003) | Não |
| `criada_por` | Autor da versão | `uuid` | 36 | - | não | FK | `Colaborador` | Preenchido quando o feedback é identificado, e deve ser o emissor (RN-003). Nulo no modo confidencial: o autor é o emissor guardado em `VinculoConfidencial` (RNF-003) | Pessoal |

#### `FeedbackFato`

Fatos que embasam cada feedback (RN-002).

**Requisitos de origem:** RF-013, RN-002

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `feedback_id` | Feedback | `uuid` | 36 | - | sim | PK, FK | `Feedback` | Todo feedback enviado tem ao menos uma linha (RN-002) | Não |
| `fato_id` | Fato vinculado | `uuid` | 36 | - | sim | PK, FK | `Fato` | Relato só com `confirmado_pelo_autor` verdadeiro (RF-012). O observado deve ser o receptor ou membro da equipe receptora* | Não |

#### `FeedbackCompetencia`

Competências tratadas em cada feedback (RF-021).

**Requisitos de origem:** RF-021

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `feedback_id` | Feedback | `uuid` | 36 | - | sim | PK, FK | `Feedback` | - | Não |
| `competencia_id` | Competência do receptor | `uuid` | 36 | - | sim | PK, FK | `Competencia` | Competência fixa do cargo ou atribuída ao receptor* (RF-021) | Não |

#### `MembroFeedbackEquipe`

Membros da equipe na data de um feedback em grupo (decisão M-09).

**Requisitos de origem:** RF-013, RF-048

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `feedback_id` | Feedback em grupo | `uuid` | 36 | - | sim | PK, FK | `Feedback` | O feedback tem `receptor_equipe_id` preenchido | Não |
| `colaborador_id` | Membro da equipe na data do feedback | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | Gravado no envio. Quem entra depois não recebe o feedback (M-09) | Pessoal |

#### `Replica`

Manifestação do receptor sobre um feedback (RF-020).

**Requisitos de origem:** RF-020

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da réplica | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `feedback_id` | Feedback comentado | `uuid` | 36 | - | sim | FK | `Feedback` | Feedback com `status = ENVIADO`* | Não |
| `autor_id` | Receptor que replica | `uuid` | 36 | - | sim | FK | `Colaborador` | Deve ser o receptor ou membro da equipe receptora* (RF-020) | Pessoal |
| `texto` | Conteúdo da réplica | `text` | 2.000* caracteres | - | sim | - | - | Não altera o conteúdo do emissor (RF-020). Orientação do RF-018 | Pessoal (R) |
| `registrada_em` | Momento do registro | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `SolicitacaoFeedback`

Pedido de feedback fora do ciclo formal (RF-031).

**Requisitos de origem:** RF-031

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da solicitação | `uuid` | 36 | - | sim | PK | `DestinatarioSolicitacao`, `Feedback` | Gerado pelo sistema | Não |
| `solicitante_id` | Quem pede o feedback | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `tema` | Assunto do pedido | `string` | 150* | - | sim | - | - | Informado pelo solicitante (RF-031) | Pessoal (R) |
| `prazo` | Data limite para resposta | `date` | data | - | sim | - | - | Posterior à data do pedido* (RF-031) | Não |
| `criada_em` | Momento do pedido | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `DestinatarioSolicitacao`

Colegas a quem a solicitação foi enviada.

**Requisitos de origem:** RF-031

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `solicitacao_id` | Solicitação | `uuid` | 36 | - | sim | PK, FK | `SolicitacaoFeedback` | Ao menos um destinatário por solicitação | Não |
| `destinatario_id` | Colega convidado a responder | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | Diferente do solicitante* | Pessoal |
| `status` | Situação do pedido para este destinatário | `enum` | `PENDENTE`, `ATENDIDA`, `RECUSADA` | - | sim | - | - | Padrão `PENDENTE`* | Não |

#### `SessaoFeedback`

Sessão de feedback agendada (RF-037 a RF-039).

**Requisitos de origem:** RF-037, RF-038, RF-039

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da sessão | `uuid` | 36 | - | sim | PK | `ParticipanteSessao` | Gerado pelo sistema | Não |
| `feedback_id` | Feedback discutido | `uuid` | 36 | - | não | FK | `Feedback` | - | Não |
| `organizador_id` | Quem agendou | `uuid` | 36 | - | sim | FK | `Colaborador` | O emissor agenda a sessão* (RF-037) | Pessoal |
| `data_hora` | Data e hora da sessão | `datetime` | data e hora | - | sim | - | - | Futura no momento do agendamento* | Não |
| `assunto` | Assunto da sessão | `string` | 150* | - | sim | - | - | (RF-037) | Pessoal (R) |
| `pauta_compartilhada` | Pauta visível a todos os participantes | `text` | 4.000* caracteres | - | não | - | - | (RF-039) | Pessoal (R) |
| `status` | Situação da sessão | `enum` | `AGENDADA`, `REALIZADA`, `CANCELADA` | - | sim | - | - | - | Não |

#### `ParticipanteSessao`

Participantes de cada sessão e suas anotações privadas (RF-039).

**Requisitos de origem:** RF-037, RF-039

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `sessao_id` | Sessão | `uuid` | 36 | - | sim | PK, FK | `SessaoFeedback` | Ao menos um participante por sessão | Não |
| `colaborador_id` | Participante | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | - | Pessoal |
| `anotacao_privada` | Anotações do participante | `text` | 4.000* caracteres | - | não | - | - | Visível só ao próprio participante (RF-039) | Pessoal (R) |

#### `DestinatarioVisibilidade`

Pessoas a quem o emissor ampliou a visibilidade de um feedback (RNF-002).

**Requisitos de origem:** RNF-002

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `feedback_id` | Feedback com visibilidade ampliada | `uuid` | 36 | - | sim | PK, FK | `Feedback` | O feedback tem `visibilidade = AMPLIADA` | Não |
| `colaborador_id` | Pessoa incluída | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | Incluída só por ação explícita do emissor (RNF-002) | Pessoal |
| `ampliada_em` | Momento da ampliação | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `DisponibilidadeAgenda`

Horários livres informados pelo colaborador, usados para sugerir o horário da sessão (RF-038).

**Requisitos de origem:** RF-038

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do horário | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `colaborador_id` | Dono da agenda | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `inicio` | Início do horário livre | `datetime` | data e hora | - | sim | - | - | Anterior a `fim` | Pessoal |
| `fim` | Fim do horário livre | `datetime` | data e hora | - | sim | - | - | Posterior a `inicio` | Pessoal |

#### `TermoOfensivo`

Lista de termos que o sistema sinaliza ao emissor antes do envio (RNF-024, decisão DS-13).

**Requisitos de origem:** RNF-024

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do termo | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `termo` | Palavra ou expressão sinalizada | `string` | 100* | - | sim | UK | - | Único. Sinaliza sem bloquear o envio (RNF-024) | Não |
| `ativo` | Indica se o termo está em uso | `bool` | verdadeiro ou falso | - | sim | - | - | - | Não |
| `cadastrado_por` | Administrador que cadastrou | `uuid` | 36 | - | sim | FK | `Colaborador` | Perfil `ADMINISTRADOR` (DS-13) | Pessoal |

### 3.4 Ciclos de avaliação, respostas e anonimato

#### `CicloAvaliacao`

Período planejado de feedback formal (RF-022).

**Requisitos de origem:** RF-022, RF-026

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do ciclo | `uuid` | 36 | - | sim | PK | `AvaliadoCiclo`, `ModalidadeCiclo`, `ObjetivoCiclo`, `ResultadoConsolidado`, `CheckIn`, `Feedback` | Gerado pelo sistema | Não |
| `titulo` | Nome do ciclo | `string` | 150* | - | sim | - | - | - | Não |
| `data_inicio` | Início do ciclo | `date` | data | - | sim | - | - | Menor ou igual a `data_fim` | Não |
| `data_fim` | Prazo de resposta | `date` | data | - | sim | - | - | Maior ou igual a `data_inicio` | Não |
| `status` | Situação do ciclo | `enum` | `StatusCiclo`: `PLANEJADO`, `ABERTO`, `ENCERRADO`, `RESULTADOS_LIBERADOS` | - | sim | - | - | Avança só nessa ordem*. A abertura notifica os avaliados (RF-026); o encerramento consolida os resultados (RF-032) | Não |
| `criado_por` | Quem planejou | `uuid` | 36 | - | sim | FK | `Colaborador` | Perfil `GESTOR` ou `RH` (RF-022) | Pessoal |
| `resultados_liberados_em` | Momento da liberação dos resultados | `datetime` | data e hora | - | não | - | - | Preenchido quando `status = RESULTADOS_LIBERADOS`* | Não |

#### `AvaliadoCiclo`

Quem é avaliado em cada ciclo (RF-022, RF-026).

**Requisitos de origem:** RF-022, RF-026

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `ciclo_id` | Ciclo | `uuid` | 36 | - | sim | PK, FK | `CicloAvaliacao` | Ao menos um avaliado por ciclo | Não |
| `avaliado_id` | Avaliado individual ou membro da equipe avaliada | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | - | Pessoal |
| `equipe_id` | Equipe, quando o receptor do ciclo é uma equipe | `uuid` | 36 | - | não | FK | `Equipe` | O avaliado deve ser membro da equipe* | Não |
| `notificado_em` | Momento da notificação de abertura | `datetime` | data e hora | - | não | - | - | Preenchido ao abrir o ciclo (RF-026) | Não |

#### `CicloCompetencia`

Competências avaliadas no ciclo (RF-022).

**Requisitos de origem:** RF-022

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `ciclo_id` | Ciclo | `uuid` | 36 | - | sim | PK, FK | `CicloAvaliacao` | - | Não |
| `competencia_id` | Competência avaliada | `uuid` | 36 | - | sim | PK, FK | `Competencia` | Competência ativa* | Não |

#### `ModalidadeCiclo`

Cada modalidade combinada no ciclo, com questionário e modo de identificação (RF-024, RF-030).

**Requisitos de origem:** RF-024, RF-025, RF-030, RN-004

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da modalidade no ciclo | `uuid` | 36 | - | sim | PK | `ConviteAvaliacao`, `RespostaAvaliacao` | Gerado pelo sistema | Não |
| `ciclo_id` | Ciclo | `uuid` | 36 | - | sim | FK | `CicloAvaliacao` | Ao menos uma modalidade por ciclo | Não |
| `modalidade` | Quem avalia quem | `enum` | `ModalidadeAvaliacao`: `GESTOR_COLABORADOR`, `ASCENDENTE`, `PARES`, `EQUIPE`, `AUTOAVALIACAO`, `AVALIACAO_360` | - | sim | - | - | Única por ciclo* (RF-024) | Não |
| `questionario_id` | Questionário aplicado | `uuid` | 36 | - | sim | FK | `Questionario` | - | Não |
| `modo_identificacao` | Modo de identificação do emissor | `enum` | `ModoIdentificacao`: `IDENTIFICADO`, `CONFIDENCIAL`, `ANONIMO` | - | sim | - | - | Só RH ou administrador configura (RF-030). `GESTOR_COLABORADOR` e `AUTOAVALIACAO` são identificados. `ASCENDENTE`, `PARES` e `EQUIPE`: padrão `CONFIDENCIAL`, com opção `ANONIMO` (RN-004; ER, seção 7) | Não |
| `peso` | Peso da modalidade no resultado | `decimal` | 0 ou mais*, 3 casas* | - | não | - | - | Maior ou igual a zero* (RF-010) | Não |
| `min_respondentes` | Mínimo de respondentes desta modalidade | `int` | inteiro positivo | respostas | sim | - | `ConfiguracaoOrganizacao.min_respondentes` | Herda o valor da organização (RN-005). Não pode ser menor que ele* | Não |

#### `ObjetivoCiclo`

Comportamento ou resultado esperado do avaliado no ciclo (RF-022, RF-023).

**Requisitos de origem:** RF-022, RF-023

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do objetivo | `uuid` | 36 | - | sim | PK | `Indicador` | Gerado pelo sistema | Não |
| `ciclo_id` | Ciclo | `uuid` | 36 | - | sim | FK | `CicloAvaliacao` | - | Não |
| `avaliado_id` | Avaliado a quem o objetivo se aplica | `uuid` | 36 | - | sim | FK | `Colaborador` | Deve estar em `AvaliadoCiclo` do mesmo ciclo* | Pessoal |
| `tipo` | Natureza do objetivo | `enum` | `COMPORTAMENTO`, `RESULTADO` | - | sim | - | - | (RF-022) | Não |
| `descricao` | Descrição do objetivo | `text` | 2.000* caracteres | - | sim | - | - | Comportamento ou resultado observável (RN-001) | Pessoal (R) |

#### `ConviteAvaliacao`

Quem foi convidado a avaliar quem, e se respondeu. Não tem ligação com a resposta (ER, seção 10).

**Requisitos de origem:** RF-025, RF-027, RF-029, RNF-012

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do convite | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `modalidade_ciclo_id` | Modalidade do ciclo | `uuid` | 36 | - | sim | FK | `ModalidadeCiclo` | - | Não |
| `avaliado_id` | Quem será avaliado | `uuid` | 36 | - | sim | FK | `Colaborador` | Deve estar em `AvaliadoCiclo`* | Pessoal |
| `avaliador_id` | Avaliador convidado | `uuid` | 36 | - | sim | FK | `Colaborador` | Na 360°, membro do time do gestor que abriu o ciclo (RF-025) | Pessoal |
| `status` | Situação do convite | `enum` | `StatusConvite`: `PENDENTE`, `RESPONDIDO`, `EXPIRADO` | - | sim | - | - | Padrão `PENDENTE`*. Não guarda o momento da mudança de status (ER, seção 10, item 2). Base do RF-029 | Não |
| `prazo` | Data limite para responder | `date` | data | - | sim | - | - | Menor ou igual a `CicloAvaliacao.data_fim`* | Não |
| `rascunho_cifrado` | Rascunho da resposta, salvo automaticamente | `text` | cifrado; tamanho da resposta* | - | não | - | - | Visível só ao avaliador. Apagado quando a resposta é enviada (RNF-012; ER, seção 10, item 4) | Pessoal (R) |

#### `RespostaAvaliacao`

Conteúdo de uma avaliação respondida (RF-027).

**Requisitos de origem:** RF-027, RF-028, RF-035

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da resposta | `uuid` | 36 | - | sim | PK | `ItemResposta`, `VinculoConfidencial` | Gerado pelo sistema. Sem FK para `ConviteAvaliacao` (decisão M-04) | Não |
| `modalidade_ciclo_id` | Modalidade do ciclo | `uuid` | 36 | - | sim | FK | `ModalidadeCiclo` | - | Não |
| `avaliado_id` | Quem foi avaliado | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `avaliador_id` | Quem respondeu | `uuid` | 36 | - | não | FK | `Colaborador` | Preenchido só no modo `IDENTIFICADO`. Nulo nos modos `CONFIDENCIAL` e `ANONIMO` (ER, seção 10) | Pessoal |
| `data_envio` | Data do envio | `date` | data, sem hora | - | sim | - | - | Só a data, para não permitir cruzar com o convite (ER, seção 10, item 2) | Não |
| `oculta_pelo_rh` | Indica se o RH ocultou a resposta do avaliado | `bool` | verdadeiro ou falso; padrão falso* | - | sim | - | `RegistroAuditoria` | Só o RH, antes da liberação dos resultados. Não apaga a resposta, registra na auditoria e avisa o emissor (RF-035) | Não |
| `motivo_ocultacao` | Motivo da ocultação | `text` | 1.000* caracteres | - | não | - | - | Obrigatório quando `oculta_pelo_rh` é verdadeiro* | Pessoal (R) |

#### `ItemResposta`

Resposta a cada pergunta (RF-009, RF-027).

**Requisitos de origem:** RF-009, RF-027

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do item | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `resposta_id` | Resposta | `uuid` | 36 | - | sim | FK | `RespostaAvaliacao` | Ao menos um item por resposta | Não |
| `pergunta_id` | Pergunta respondida | `uuid` | 36 | - | sim | FK | `Pergunta` | Pergunta do questionário da modalidade* | Não |
| `valor_numerico` | Valor da escala ou número | `decimal` | entre `escala_min` e `escala_max` na escala ordinal | - | não | - | - | Usado quando `tipo_resposta` é `ESCALA_ORDINAL` ou `NUMERICO`* | Pessoal |
| `atingido` | Atingido ou não atingido | `bool` | verdadeiro ou falso | - | não | - | - | Usado quando `tipo_resposta = ATINGIDO_NAO_ATINGIDO`* | Pessoal |
| `valor_texto` | Resposta em texto livre | `text` | 4.000* caracteres | - | não | - | - | Usado quando `tipo_resposta = TEXTO_LIVRE`*. Orientação do RF-018. Nos modos não identificados, exibido sem autor e só com o mínimo de respondentes (ER, seção 10, item 6) | Pessoal (R) |

Regra comum: exatamente um campo de valor preenchido, conforme o `tipo_resposta` da pergunta*, e preenchimento obrigatório quando `Pergunta.obrigatoria` é verdadeiro*.

#### `VinculoConfidencial`

Identidade do emissor no modo confidencial, guardada em esquema separado, com chave de criptografia própria (RNF-003, decisão M-04).

**Requisitos de origem:** RNF-003, RN-004

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do vínculo | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `origem` | Tipo de registro vinculado | `enum` | `RESPOSTA`, `FEEDBACK` | - | sim | - | - | - | Não |
| `referencia_id` | Registro vinculado | `uuid` | 36 | - | sim | - | `RespostaAvaliacao` ou `Feedback`, conforme `origem` | Sem FK declarada, porque fica em esquema separado. No máximo um vínculo por registro* | Não |
| `emissor_id` | Emissor confidencial | `uuid` | 36 | - | sim | FK | `Colaborador` | Criado só no modo `CONFIDENCIAL`. Toda leitura gera `RegistroAuditoria` com `acao = CONSULTA_IDENTIDADE` (RNF-003, RNF-005). O RH nunca lê vínculos de avaliações em que ele é o avaliado (RN-004) | Pessoal (C) |
| `criado_em` | Momento da criação | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema | Não |

#### `ResultadoConsolidado`

Resultado calculado ao encerrar o ciclo e guardado (RF-032, decisão M-08).

**Requisitos de origem:** RF-032, RF-033, RF-049, RF-050, RF-052, RN-005, RN-008, RNF-007

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do resultado | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `ciclo_id` | Ciclo | `uuid` | 36 | - | sim | FK | `CicloAvaliacao` | - | Não |
| `avaliado_id` | Avaliado | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `modalidade` | Fonte do resultado | `enum` | `ModalidadeAvaliacao` ou `AGREGADO` | - | sim | - | - | `AGREGADO` reúne fontes abaixo do mínimo de respondentes (RN-005) | Não |
| `competencia_id` | Competência do resultado | `uuid` | 36 | - | não | FK | `Competencia` | - | Não |
| `indicador_id` | Indicador do resultado | `uuid` | 36 | - | não | FK | `Indicador` | - | Não |
| `valor` | Valor consolidado | `decimal` | conforme a escala* | - | sim | - | - | Apoio à decisão humana. Critérios e dados do cálculo exibíveis (RN-008) | Pessoal |
| `num_respostas` | Número de respostas consideradas | `int` | 1 ou mais | respostas | sim | - | - | Em fontes confidenciais ou anônimas, só exibido se for maior ou igual ao mínimo (RN-005). Exibido junto com o valor (RNF-007) | Não |
| `calculado_em` | Momento do cálculo | `datetime` | data e hora | - | sim | - | - | Não é recalculado depois da liberação (M-08) | Não |

### 3.5 Metas, indicadores, check-ins e planos de ação

#### `Meta`

Meta de desenvolvimento individual ou de equipe (RF-046, RF-047).

**Requisitos de origem:** RF-046, RF-047

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da meta | `uuid` | 36 | - | sim | PK | `Indicador` | Gerado pelo sistema | Não |
| `escopo` | Meta individual ou de equipe | `enum` | `INDIVIDUAL`, `EQUIPE` | - | sim | - | - | - | Não |
| `colaborador_id` | Colaborador da meta individual | `uuid` | 36 | - | não | FK | `Colaborador` | Obrigatório se `escopo = INDIVIDUAL` e nulo se `EQUIPE`* (RF-046) | Pessoal |
| `equipe_id` | Equipe da meta de equipe | `uuid` | 36 | - | não | FK | `Equipe` | Obrigatório se `escopo = EQUIPE` e nulo se `INDIVIDUAL`* (RF-047) | Não |
| `competencia_id` | Competência relacionada | `uuid` | 36 | - | não | FK | `Competencia` | (RF-046) | Não |
| `descricao` | Descrição da meta | `text` | 2.000* caracteres | - | sim | - | - | Orientação do RF-018* | Pessoal (R) |
| `data_inicio` | Início | `date` | data | - | sim* | - | - | Menor ou igual a `prazo` | Não |
| `prazo` | Data limite | `date` | data | - | sim | - | - | Maior ou igual a `data_inicio` (RF-046) | Não |
| `status` | Situação da meta | `enum` | `StatusMeta`: `EM_ANDAMENTO`, `ATINGIDA`, `NAO_ATINGIDA`, `CANCELADA` | - | sim | - | - | Único registro do resultado da meta (RF-047) | Pessoal |
| `criada_por` | Quem cadastrou | `uuid` | 36 | - | sim | FK | `Colaborador` | Colaborador ou gestor, na meta individual; gestor ou membro da equipe, na meta de equipe (RF-046, RF-047, RN-006) | Pessoal |

#### `Indicador`

Medida de um objetivo de ciclo ou de uma meta (RF-023, decisão M-05).

**Requisitos de origem:** RF-023, RF-046, RF-049

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do indicador | `uuid` | 36 | - | sim | PK | `MedicaoIndicador`, `ResultadoConsolidado` | Gerado pelo sistema | Não |
| `objetivo_id` | Objetivo de ciclo medido | `uuid` | 36 | - | não | FK | `ObjetivoCiclo` | Exatamente um entre `objetivo_id` e `meta_id` (ER, seção 8) | Não |
| `meta_id` | Meta medida | `uuid` | 36 | - | não | FK | `Meta` | Exatamente um entre `objetivo_id` e `meta_id` | Não |
| `descricao` | O que é medido | `string` | 255* | - | sim | - | - | - | Não |
| `tipo_valor` | Formato do valor | `enum` | `TipoResposta` | - | sim | - | - | (RF-009) | Não |
| `valor_esperado` | Valor que indica o objetivo atingido | `string` | 100* | - | sim | - | - | Compatível com `tipo_valor`* (RF-023) | Não |
| `fonte_evidencia` | De onde vem o dado medido | `string` | 255* | - | não* | - | - | Obrigatório para indicador de objetivo de ciclo* (RF-023) | Não |
| `peso` | Peso do indicador | `decimal` | 0 ou mais*, 3 casas* | - | não | - | - | Maior ou igual a zero* (RF-010) | Não |

#### `MedicaoIndicador`

Valor observado de um indicador em uma data (RF-023, RF-049).

**Requisitos de origem:** RF-023, RF-049

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da medição | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `indicador_id` | Indicador medido | `uuid` | 36 | - | sim | FK | `Indicador` | - | Não |
| `checkin_id` | Check-in em que foi medido | `uuid` | 36 | - | não | FK | `CheckIn` | - | Não |
| `valor_observado` | Valor medido | `string` | 100* | - | sim | - | - | Compatível com `Indicador.tipo_valor`* | Pessoal |
| `data_medicao` | Data da medição | `date` | data | - | sim | - | - | Não futura* | Não |
| `registrada_por` | Quem registrou | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |

#### `ConfiguracaoCheckIn`

Regra de check-ins periódicos definida pelo gestor (RF-041, RF-036).

**Requisitos de origem:** RF-036, RF-041

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da configuração | `uuid` | 36 | - | sim | PK | `CheckIn` | Gerado pelo sistema | Não |
| `gestor_id` | Gestor que configurou | `uuid` | 36 | - | sim | FK | `Colaborador` | Perfil `GESTOR` (RF-041) | Pessoal |
| `colaborador_id` | Colaborador incluído nos check-ins | `uuid` | 36 | - | sim | FK | `Colaborador` | Membro da equipe do gestor (RF-041, P-09) | Pessoal |
| `frequencia` | Periodicidade | `enum` | `FrequenciaCheckIn`: `SEMANAL`, `QUINZENAL`, `MENSAL` | - | sim | - | - | Configurável pelo gestor (RF-041) | Não |
| `questionario_id` | Perguntas do check-in | `uuid` | 36 | - | não | FK | `Questionario` | Perguntas alternáveis entre períodos (RF-036) | Não |
| `ativa` | Indica se a configuração está em vigor | `bool` | verdadeiro ou falso | - | sim | - | - | - | Não |

#### `CheckIn`

Check-in realizado ou previsto (RF-023, RF-041).

**Requisitos de origem:** RF-023, RF-041

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do check-in | `uuid` | 36 | - | sim | PK | `MedicaoIndicador` | Gerado pelo sistema | Não |
| `configuracao_id` | Configuração periódica de origem | `uuid` | 36 | - | não | FK | `ConfiguracaoCheckIn` | Exatamente um entre `configuracao_id` e `ciclo_id`* | Não |
| `ciclo_id` | Ciclo de origem | `uuid` | 36 | - | não | FK | `CicloAvaliacao` | Exatamente um entre `configuracao_id` e `ciclo_id`* | Não |
| `gestor_id` | Gestor do check-in | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `colaborador_id` | Colaborador do check-in | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `data_prevista` | Data planejada | `date` | data | - | sim | - | - | - | Não |
| `data_realizada` | Data em que ocorreu | `date` | data | - | não | - | - | Não futura* | Não |
| `anotacoes` | Registro do check-in | `text` | 4.000* caracteres | - | não | - | - | Orientação do RF-018* | Pessoal (R) |

#### `CheckInMeta`

Metas em andamento acompanhadas em um check-in periódico (RF-041).

**Requisitos de origem:** RF-041

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `checkin_id` | Check-in | `uuid` | 36 | - | sim | PK, FK | `CheckIn` | - | Não |
| `meta_id` | Meta acompanhada | `uuid` | 36 | - | sim | PK, FK | `Meta` | Meta do colaborador do check-in, com `status = EM_ANDAMENTO`* | Não |

#### `CheckInPlano`

Planos de ação em andamento acompanhados em um check-in periódico (RF-041).

**Requisitos de origem:** RF-041

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `checkin_id` | Check-in | `uuid` | 36 | - | sim | PK, FK | `CheckIn` | - | Não |
| `plano_id` | Plano acompanhado | `uuid` | 36 | - | sim | PK, FK | `PlanoAcao` | Plano do colaborador do check-in, ainda não concluído* | Não |

#### `PlanoAcao`

Plano criado a partir de um feedback construtivo (RF-042, RF-043).

**Requisitos de origem:** RF-042, RF-043, RF-044, RF-045, RN-006

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do plano | `uuid` | 36 | - | sim | PK | `AcaoPlano`, `PontoMonitoramento` | Gerado pelo sistema | Não |
| `feedback_id` | Feedback de origem | `uuid` | 36 | - | sim | FK, UK | `Feedback` | Feedback do tipo `CONSTRUTIVO` (RF-042). No máximo um plano por feedback | Não |
| `receptor_id` | Receptor do feedback | `uuid` | 36 | - | sim | FK | `Colaborador` | Igual ao receptor do feedback de origem* (RN-006) | Pessoal |
| `emissor_id` | Emissor do feedback | `uuid` | 36 | - | não | FK | `Colaborador` | Igual ao emissor do feedback de origem quando ele é identificado (RN-006). Nulo se o feedback de origem é confidencial (RN-004, ERS-D05) | Pessoal |
| `gestor_id` | Gestor direto do receptor | `uuid` | 36 | - | não | FK | `Colaborador` | Obrigatório quando o feedback de origem é confidencial: o plano é definido pelo receptor e pelo gestor direto, sem o emissor (RN-006, ERS-D05) | Pessoal |
| `data_final` | Data de verificação final | `date` | data | - | sim | - | - | (RF-042) | Não |
| `status` | Situação do plano | `enum` | `StatusPlano`: `AGUARDANDO_CONFIRMACAO`, `ABERTO`, `EM_ACOMPANHAMENTO`, `CONCLUIDO` | - | sim | - | - | Fica em `AGUARDANDO_CONFIRMACAO` até o receptor confirmar o plano registrado pelo emissor (RN-006, decisão UC19-D01) | Não |
| `resultado_final` | Desfecho na data final | `enum` | `MELHOROU`, `NOVO_FEEDBACK` | - | não | - | - | Obrigatório para concluir o plano* (RF-043). Base do RF-045 | Pessoal |
| `conclusao` | Comentário final | `text` | 2.000* caracteres | - | não | - | - | Orientação do RF-018* | Pessoal (R) |

#### `AcaoPlano`

Ações de um plano (RF-042).

**Requisitos de origem:** RF-042

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da ação | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `plano_id` | Plano | `uuid` | 36 | - | sim | FK | `PlanoAcao` | Ao menos uma ação por plano | Não |
| `descricao` | O que será feito | `text` | 1.000* caracteres | - | sim | - | - | - | Pessoal (R) |
| `responsavel_id` | Responsável pela ação | `uuid` | 36 | - | sim | FK | `Colaborador` | (RF-042) | Pessoal |
| `meta_acao` | Resultado esperado da ação | `string` | 255* | - | não* | - | - | (RF-042) | Não |
| `prazo` | Data limite da ação | `date` | data | - | sim* | - | - | Menor ou igual a `PlanoAcao.data_final`* | Não |
| `status` | Situação da ação | `enum` | `PENDENTE`, `EM_ANDAMENTO`, `CONCLUIDA` | - | sim | - | - | - | Não |

#### `PontoMonitoramento`

Ponto de verificação do plano (RF-042, RF-043).

**Requisitos de origem:** RF-042, RF-043

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do ponto | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `plano_id` | Plano | `uuid` | 36 | - | sim | FK | `PlanoAcao` | Ao menos um ponto por plano | Não |
| `data_prevista` | Data planejada | `date` | data | - | sim | - | - | Menor ou igual a `PlanoAcao.data_final`* | Não |
| `resultado` | Resultado registrado | `text` | 2.000* caracteres | - | não | - | - | (RF-043) | Pessoal (R) |
| `data_registro` | Data do registro do resultado | `date` | data | - | não | - | - | Obrigatório quando `resultado` está preenchido* | Não |

### 3.6 LGPD, auditoria e notificações

#### `CategoriaDado`

Inventário das categorias de dados e da política de retenção (RF-054, RF-062).

**Requisitos de origem:** RF-054, RF-062, RNF-032

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da categoria | `uuid` | 36 | - | sim | PK | `CompartilhamentoDados` | Gerado pelo sistema | Não |
| `nome` | Nome da categoria | `string` | 100* | - | sim | UK | - | Exemplos do ER: cadastro, feedbacks, planos, acessos | Não |
| `finalidade` | Para que os dados são tratados | `text` | 1.000* caracteres | - | sim | - | - | (RF-054) | Não |
| `base_legal` | Base legal do tratamento | `enum` | `BaseLegal`: `EXECUCAO_CONTRATO`, `LEGITIMO_INTERESSE`, `OBRIGACAO_LEGAL`, `CONSENTIMENTO`, `EXERCICIO_DIREITOS` | - | sim | - | - | `CONSENTIMENTO` só para funções opcionais (RN-012) | Não |
| `prazo_retencao_meses` | Prazo de guarda | `int` | inteiro positivo | meses | sim | - | - | Feedbacks, avaliações e planos: padrão 60 meses após o desligamento (RN-011). Registros de acesso: no mínimo 6 meses (RNF-032) | Não |
| `acao_fim_prazo` | O que fazer ao fim do prazo | `enum` | `ELIMINAR`, `ANONIMIZAR` | - | sim | - | - | Suspensa enquanto houver `BloqueioLegal` ativo (RF-062) | Não |

#### `CompartilhamentoDados`

Entidades com quem os dados são compartilhados (RF-060).

**Requisitos de origem:** RF-060, RN-016

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do compartilhamento | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `categoria_id` | Categoria compartilhada | `uuid` | 36 | - | sim | FK | `CategoriaDado` | - | Não |
| `entidade_destino` | Quem recebe os dados | `string` | 150* | - | sim | - | - | (RF-060) | Não |
| `tipo_entidade` | Natureza de quem recebe | `enum` | `PUBLICA`, `PRIVADA` | - | sim | - | - | (RF-060) | Não |
| `finalidade` | Para que os dados são compartilhados | `text` | 1.000* caracteres | - | sim | - | - | - | Não |
| `inclui_menores` | Indica se o compartilhamento abrange dados de menores de 18 anos | `bool` | verdadeiro ou falso; padrão falso | - | sim | - | - | Verdadeiro só com justificativa (RN-016; LGPD, art. 14) | Não |
| `justificativa_menores` | Por que os dados de menores são necessários | `text` | 1.000* caracteres | - | não | - | - | Obrigatória quando `inclui_menores` é verdadeiro (RN-016) | Não |
| `data_inicio` | Início do compartilhamento | `date` | data | - | sim | - | - | - | Não |
| `data_fim` | Fim do compartilhamento | `date` | data | - | não | - | - | Maior ou igual a `data_inicio`* | Não |

#### `BloqueioLegal`

Suspensão da eliminação por processo judicial (RF-062).

**Requisitos de origem:** RF-062

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do bloqueio | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `colaborador_id` | Titular cujos dados ficam bloqueados | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `numero_processo` | Número do processo judicial | `string` | 25* (número único do CNJ, com máscara*) | - | sim | - | - | Formato do número único de processo* | Pessoal |
| `data_inicio` | Início do bloqueio | `date` | data | - | sim | - | - | - | Não |
| `data_fim` | Fim do bloqueio | `date` | data | - | não | - | - | Enquanto vazio, a eliminação fica suspensa (RF-062) | Não |

#### `TermoConsentimento`

Versão de um termo de consentimento para função opcional (RF-055).

**Requisitos de origem:** RF-055, RN-012

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do termo | `uuid` | 36 | - | sim | PK | `Consentimento` | Gerado pelo sistema | Não |
| `finalidade` | Função opcional coberta | `text` | 1.000* caracteres | - | sim | - | - | Só funcionalidade opcional (RN-012) | Não |
| `versao` | Versão do termo | `string` | 20* | - | sim | - | - | Única por finalidade* (RF-055) | Não |
| `texto` | Texto apresentado ao titular | `text` | 20.000* caracteres | - | sim | - | - | Linguagem clara (RNF-016) | Não |
| `vigente_desde` | Início da vigência | `date` | data | - | sim | - | - | - | Não |

#### `Consentimento`

Registro de quem consentiu, quando e em qual versão (RF-055).

**Requisitos de origem:** RF-055, RN-012

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do consentimento | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `colaborador_id` | Titular que consentiu | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `termo_id` | Termo aceito | `uuid` | 36 | - | sim | FK | `TermoConsentimento` | Termo vigente no momento* | Não |
| `concedido_em` | Momento do consentimento | `datetime` | data e hora | - | sim | - | - | (RF-055) | Pessoal |
| `revogado_em` | Momento da revogação | `datetime` | data e hora | - | não | - | - | Maior que `concedido_em`*. Revogação por meio tão simples quanto o consentimento (RF-055). Recusar ou revogar não bloqueia o uso (RN-012) | Pessoal |

#### `SolicitacaoTitular`

Pedido do titular para exercer um direito da LGPD (RF-056 a RF-061).

**Requisitos de origem:** RF-056, RF-057, RF-058, RF-059, RF-061

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da solicitação | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `titular_id` | Titular que pediu | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `tipo` | Direito exercido | `enum` | `TipoSolicitacaoTitular`: `CONFIRMACAO_ACESSO`, `CORRECAO`, `ANONIMIZACAO_BLOQUEIO_ELIMINACAO`, `PORTABILIDADE`, `INFORMACAO_COMPARTILHAMENTO`, `REVOGACAO_CONSENTIMENTO` | - | sim | - | - | (RF-056 a RF-060) | Pessoal |
| `aberta_em` | Momento da abertura | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema (RF-061) | Não |
| `prazo` | Data limite de resposta | `date` | data | - | sim | - | - | 15 dias para a declaração completa (RF-056). Os demais prazos são definidos pela organização (ERS-D10) | Não |
| `status` | Situação | `enum` | `ABERTA`, `EM_ANALISE`, `ATENDIDA`, `NEGADA` | - | sim | - | - | (RF-061) | Não |
| `responsavel_id` | Quem trata a solicitação | `uuid` | 36 | - | não | FK | `Colaborador` | RH ou encarregado (RF-061) | Pessoal |
| `resposta` | Resposta enviada ao titular | `text` | 10.000* caracteres | - | não | - | - | Obrigatória quando `status` é `ATENDIDA` ou `NEGADA`*. Não revela emissores confidenciais (RF-056) | Pessoal (R) |
| `respondida_em` | Momento da resposta | `datetime` | data e hora | - | não | - | - | Maior ou igual a `aberta_em`* | Não |

#### `IncidenteSeguranca`

Registro de incidente de segurança com dados pessoais (RF-063).

**Requisitos de origem:** RF-063

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do incidente | `uuid` | 36 | - | sim | PK | `TitularAfetado` | Gerado pelo sistema | Não |
| `detectado_em` | Momento da detecção | `datetime` | data e hora | - | sim | - | - | (RF-063) | Não |
| `descricao` | Descrição do incidente | `text` | 4.000* caracteres | - | sim | - | - | - | Pessoal (R) |
| `dados_afetados` | Dados atingidos | `text` | 2.000* caracteres | - | sim | - | - | (RF-063) | Pessoal (R) |
| `medidas_adotadas` | Medidas tomadas | `text` | 4.000* caracteres | - | sim* | - | - | (RF-063) | Não |
| `comunicado_anpd` | Indica se a ANPD foi comunicada | `bool` | verdadeiro ou falso; padrão falso* | - | sim | - | - | - | Não |
| `guardar_ate` | Data até a qual o registro é guardado | `date` | data | - | sim | - | - | No mínimo 5 anos após `detectado_em` (RF-063) | Não |

#### `TitularAfetado`

Titulares atingidos por um incidente (RF-063).

**Requisitos de origem:** RF-063

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `incidente_id` | Incidente | `uuid` | 36 | - | sim | PK, FK | `IncidenteSeguranca` | - | Não |
| `colaborador_id` | Titular afetado | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | - | Pessoal |
| `comunicado_em` | Momento da comunicação ao titular | `datetime` | data e hora | - | não | - | - | - | Não |

#### `RegistroAuditoria`

Trilha de auditoria. Somente inclusão: sem alteração nem exclusão (RNF-005).

**Requisitos de origem:** RNF-005, RF-035

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador do registro | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `ator_id` | Quem fez a ação | `uuid` | 36 | - | sim | FK | `Colaborador` | (RNF-005: "quem") | Pessoal |
| `data_hora` | Momento da ação | `datetime` | data e hora | - | sim | - | - | Gerado pelo sistema (RNF-005: "quando") | Não |
| `acao` | Ação registrada | `enum` | `AcaoAuditoria`: `CONSULTA`, `CRIACAO`, `ALTERACAO`, `OCULTACAO`, `CONSULTA_IDENTIDADE`, `EXPORTACAO`, `ANONIMIZACAO`, `ELIMINACAO` | - | sim | - | - | Toda leitura de `VinculoConfidencial` gera `CONSULTA_IDENTIDADE` (RNF-003). Exportação, anonimização e eliminação de dados também são registradas (RF-058, RF-062) | Não |
| `entidade` | Entidade afetada | `string` | 60* | - | sim | - | - | Nome de entidade do ER* (RNF-005: "o quê") | Não |
| `entidade_id` | Registro afetado | `uuid` | 36 | - | sim | - | Qualquer entidade | - | Não |
| `ip_origem` | Endereço IP de origem | `string` | 45* (IPv4 ou IPv6) | - | sim | - | - | Endereço IP válido* (RNF-005: "de onde"; RNF-032) | Pessoal |
| `detalhes` | Informações adicionais | `text` | 4.000* caracteres | - | não | - | - | Não copia o conteúdo do feedback nem a identidade consultada* | Pessoal (R) |
| `hash_anterior` | Resumo do registro anterior | `string` | 64* (SHA-256 em hexadecimal*) | - | sim | - | `RegistroAuditoria` anterior | Encadeamento que torna a trilha inalterável (RNF-005) | Não |

#### `Notificacao`

Notificações e lembretes enviados ou agendados (RF-026, RF-037, RF-040).

**Requisitos de origem:** RF-026, RF-037, RF-040

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `id` | Identificador da notificação | `uuid` | 36 | - | sim | PK | - | Gerado pelo sistema | Não |
| `destinatario_id` | Quem recebe | `uuid` | 36 | - | sim | FK | `Colaborador` | - | Pessoal |
| `tipo` | Tipo da notificação | `enum` | `TipoNotificacao`: `SESSAO_AGENDADA`, `LEMBRETE_SESSAO`, `AVALIACAO_PENDENTE`, `CHECKIN`, `PRAZO_PLANO`, `CICLO_ABERTO`, `RESPOSTA_OCULTADA`, `FEEDBACK_RECEBIDO`, `PLANO_PARA_CONFIRMAR` | - | sim | - | `PreferenciaNotificacao` | Lembretes não são enviados a quem os desativou (RF-040) | Não |
| `entidade` | Entidade de origem | `string` | 60* | - | sim | - | - | Nome de entidade do ER* | Não |
| `entidade_id` | Registro de origem | `uuid` | 36 | - | sim | - | Qualquer entidade | - | Não |
| `agendada_para` | Momento previsto do envio | `datetime` | data e hora | - | sim | - | - | - | Não |
| `enviada_em` | Momento do envio | `datetime` | data e hora | - | não | - | - | Maior ou igual a `agendada_para`* | Não |
| `lida` | Indica se foi lida | `bool` | verdadeiro ou falso; padrão falso* | - | sim | - | - | - | Não |

#### `PreferenciaNotificacao`

Lembretes que cada usuário mantém ativos (RF-040).

**Requisitos de origem:** RF-040

| Atributo | Definição | Tipo | Tamanho ou domínio | Unid. | Obr. | Chave | Relacionamento | Regra de validação | Dado pessoal |
|---|---|---|---|---|---|---|---|---|---|
| `colaborador_id` | Usuário | `uuid` | 36 | - | sim | PK, FK | `Colaborador` | - | Pessoal |
| `tipo` | Tipo de notificação | `enum` | `TipoNotificacao` | - | sim | PK | - | - | Não |
| `ativa` | Indica se o usuário quer receber | `bool` | verdadeiro ou falso; padrão verdadeiro* | - | sim | - | - | Cada usuário pode desativar (RF-040) | Não |

### 3.7 Enumerações

As enumerações com nome (`Perfil`, `TipoFeedback`, `ModoIdentificacao` e outras) estão na [seção 11 do modelo ER](modelagem/modelo-dados/Modelo_Dominio_ER.md#11-dicionário-de-enumerações) e foram repetidas nas tabelas acima. As enumerações abaixo aparecem só dentro dos diagramas do ER, sem nome próprio:

| Atributo | Valores no ER | Observação |
|---|---|---|
| `Feedback.modalidade` | `FORMAL`, `INFORMAL` | - |
| `Feedback.status` | `RASCUNHO`, `ENVIADO` | - |
| `DestinatarioSolicitacao.status` | `PENDENTE`, `ATENDIDA`, `RECUSADA` | - |
| `SessaoFeedback.status` | `AGENDADA`, `REALIZADA`, `CANCELADA` | - |
| `ObjetivoCiclo.tipo` | `COMPORTAMENTO`, `RESULTADO` | - |
| `VinculoConfidencial.origem` | `RESPOSTA`, `FEEDBACK` | - |
| `ResultadoConsolidado.modalidade` | valores de `ModalidadeAvaliacao` e `AGREGADO` | `AGREGADO` reúne fontes abaixo do mínimo (RN-005) |
| `Meta.escopo` | `INDIVIDUAL`, `EQUIPE` | - |
| `PlanoAcao.resultado_final` | `MELHOROU`, `NOVO_FEEDBACK` | - |
| `AcaoPlano.status` | `PENDENTE`, `EM_ANDAMENTO`, `CONCLUIDA` | - |
| `CategoriaDado.acao_fim_prazo` | `ELIMINAR`, `ANONIMIZAR` | - |
| `CompartilhamentoDados.tipo_entidade` | `PUBLICA`, `PRIVADA` | - |
| `SolicitacaoTitular.status` | `ABERTA`, `EM_ANALISE`, `ATENDIDA`, `NEGADA` | - |

---

## 4. Dados pessoais e sensíveis (LGPD)

### 4.1 Critério de classificação

| Classificação | Quando é usada |
|---|---|
| **Não** | O atributo, sozinho, não identifica nem descreve uma pessoa. Exemplos: configurações, catálogos, datas técnicas |
| **Pessoal** | O atributo identifica uma pessoa ou descreve algo sobre ela: cadastro, chaves que apontam para um colaborador, avaliações e resultados de alguém (LGPD, art. 5º, I) |
| **Pessoal (R)** | Texto livre sobre pessoas. É dado pessoal e tem **risco** de conter dado sensível por descuido de quem escreve (RF-018) |
| **Pessoal (C)** | Identidade de **acesso restrito**: emissor confidencial ou quem relatou um fato. Não pode chegar ao receptor (RN-004, RNF-003, RF-012) |

**Não há atributo classificado como sensível.** A RN-013 proíbe criar campos para dados pessoais sensíveis, e o ER segue essa regra (ER, seção 4). O risco de dado sensível vem só dos textos livres (seção 4.3).

Quando um atributo marcado como `Não` é lido junto com o registro de uma pessoa, ele passa a fazer parte de um dado pessoal. A classificação acima vale para o atributo isolado e serve para priorizar os controles.

### 4.2 Inventário dos dados pessoais

A base legal indicada é a **provável**, segundo a RN-012 e a pesquisa documental (seção 3.3). A decisão final é do controlador, que a registra em `CategoriaDado.base_legal` (RF-054).

| Grupo | Atributos | Finalidade | Base legal provável | Retenção |
|---|---|---|---|---|
| **Cadastro e acesso** | `Colaborador`: `id`, `matricula`, `nome`, `email`, `senha_hash`, `falhas_login_consecutivas`, `login_bloqueado_ate`, `data_nascimento`, `data_admissao`, `data_desligamento`, `situacao`, `cargo_id`, `equipe_id`, `gestor_id`. `PerfilColaborador`: todos. `Equipe.gestor_id` | Identificar o usuário, controlar o acesso por perfil e montar a hierarquia que define a visibilidade (RF-001, RF-003, RNF-001) | Execução de contrato (RN-012) | Definida pela organização, por categoria (RF-062, ERS-D10) |
| **Fatos e feedbacks** | `Fato`: `autor_id`, `observado_id`, `data_ocorrencia`, `descricao`. `Feedback`: `emissor_id`, `receptor_colaborador_id`, `tipo`, `postura_receptor`, `agregou_valor`. `VersaoFeedback`: campos de texto e `criada_por`. `MembroFeedbackEquipe.colaborador_id`. `Replica`: `autor_id`, `texto`. `SolicitacaoFeedback`: `solicitante_id`, `tema`. `DestinatarioSolicitacao.destinatario_id`. `SessaoFeedback`: `organizador_id`, `assunto`, `pauta_compartilhada`. `ParticipanteSessao`: `colaborador_id`, `anotacao_privada`. `DestinatarioVisibilidade.colaborador_id`. `DisponibilidadeAgenda`: `colaborador_id`, `inicio`, `fim`. `CompetenciaAtribuida`: `colaborador_id`, `atribuida_por`, `justificativa`. `Pergunta.colaborador_alvo_id` | Apoiar o desenvolvimento profissional do colaborador (RN-007) | Execução de contrato ou legítimo interesse (RN-012) | Enquanto o colaborador estiver na organização e por 5 anos (60 meses) após o desligamento, configurável. Depois, eliminar ou anonimizar (RN-011, RF-062) |
| **Avaliações de ciclo** | `CicloAvaliacao.criado_por`. `AvaliadoCiclo.avaliado_id`. `ObjetivoCiclo`: `avaliado_id`, `descricao`. `ConviteAvaliacao`: `avaliado_id`, `avaliador_id`, `rascunho_cifrado`. `RespostaAvaliacao`: `avaliado_id`, `avaliador_id`, `motivo_ocultacao`. `ItemResposta`: `valor_numerico`, `atingido`, `valor_texto`. `ResultadoConsolidado`: `avaliado_id`, `valor` | Avaliar o desempenho por competência e indicador, como apoio à decisão humana (RN-008) | Execução de contrato ou legítimo interesse (RN-012) | Igual aos feedbacks (RN-011). O rascunho é apagado no envio da resposta (RNF-012; ER, seção 10) |
| **Metas, check-ins e planos** | `Meta`: `colaborador_id`, `descricao`, `status`, `criada_por`. `MedicaoIndicador`: `valor_observado`, `registrada_por`. `ConfiguracaoCheckIn`: `gestor_id`, `colaborador_id`. `CheckIn`: `gestor_id`, `colaborador_id`, `anotacoes`. `PlanoAcao`: `receptor_id`, `emissor_id`, `gestor_id`, `resultado_final`, `conclusao`. `AcaoPlano`: `descricao`, `responsavel_id`. `PontoMonitoramento.resultado` | Acompanhar a melhora do colaborador (RF-043, RF-046) | Execução de contrato ou legítimo interesse (RN-012) | Planos: RN-011. Metas e check-ins: definidos pela organização (RF-062, ERS-D10) |
| **Direitos do titular e LGPD** | `Consentimento`: `colaborador_id`, `concedido_em`, `revogado_em`. `SolicitacaoTitular`: `titular_id`, `tipo`, `responsavel_id`, `resposta`. `BloqueioLegal`: `colaborador_id`, `numero_processo`. `TitularAfetado.colaborador_id`. `IncidenteSeguranca`: `descricao`, `dados_afetados`. `ConfiguracaoOrganizacao`: `encarregado_nome`, `encarregado_contato` | Cumprir e comprovar as obrigações da LGPD (RF-053, RF-055 a RF-063) | Obrigação legal. Para o bloqueio judicial, exercício regular de direitos em processo | Incidentes: no mínimo 5 anos (RF-063). Bloqueio: até `data_fim`. Demais: definidos pela organização (RF-062, ERS-D10) |
| **Auditoria, importação e notificações** | `RegistroAuditoria`: `ator_id`, `ip_origem`, `detalhes`. `ImportacaoCadastro`: `executada_por`, `log_erros`. `Questionario.criado_por`. `Notificacao.destinatario_id`. `PreferenciaNotificacao.colaborador_id`. `TermoOfensivo.cadastrado_por` | Segurança, responsabilização e envio de lembretes (RNF-005, RF-040) | Registros de acesso: obrigação legal, se o sistema for operado como serviço (RNF-032). Demais: legítimo interesse | Registros de acesso: no mínimo 6 meses (RNF-032). Demais: definidos pela organização (RF-062, ERS-D10) |

### 4.3 Textos livres e risco de dado sensível

O sistema não coleta dado sensível em campo próprio (RN-013). Mesmo assim, quem escreve um feedback pode citar, sem querer, uma doença, uma religião ou a vida pessoal de alguém. Por isso, estes atributos de texto livre são classificados como `Pessoal (R)`:

| Área | Atributos |
|---|---|
| Fatos e feedbacks | `Fato.descricao`; `VersaoFeedback`: `descricao`, `acao_comportamento`, `resultados`, `repercussao`, `aspecto_positivo`, `problema`, `reflexao`; `Replica.texto`; `SolicitacaoFeedback.tema`; `SessaoFeedback`: `assunto`, `pauta_compartilhada`; `ParticipanteSessao.anotacao_privada`; `CompetenciaAtribuida.justificativa` |
| Avaliações | `ObjetivoCiclo.descricao`; `ConviteAvaliacao.rascunho_cifrado`; `RespostaAvaliacao.motivo_ocultacao`; `ItemResposta.valor_texto` |
| Metas e planos | `Meta.descricao`; `CheckIn.anotacoes`; `PlanoAcao.conclusao`; `AcaoPlano.descricao`; `PontoMonitoramento.resultado` |
| LGPD e auditoria | `SolicitacaoTitular.resposta`; `IncidenteSeguranca`: `descricao`, `dados_afetados`; `RegistroAuditoria.detalhes` |

**Controles já previstos na lista geral:**

- orientação ao emissor para descrever fatos observáveis e não incluir dados sensíveis, de saúde ou de terceiros (RF-018);
- feedback baseado em fatos, nunca em personalidade ou vida privada (RN-001);
- sinalização de termos ofensivos ou discriminatórios antes do envio, sem bloquear (RNF-024, Could);
- proibição de usar dados individuais de feedback para monitorar a saúde do colaborador (RN-015);
- criptografia em trânsito e em repouso (RNF-004);
- nos modos não identificados, texto livre exibido sem autor e só com o mínimo de respondentes, porque o próprio texto pode revelar quem escreveu (RN-005; ER, seção 10, item 6).

### 4.4 Identidade do emissor confidencial e de quem relatou

Atributos `Pessoal (C)`. Só o RH pode chegar a eles, com registro na trilha de auditoria (RNF-003, RNF-005). O RH nunca consulta a identidade de quem o avaliou (RN-004). O administrador não tem acesso (Especificação Suplementar, seção 8.1).

| Atributo | Por que é restrito | Regra |
|---|---|---|
| `VinculoConfidencial.emissor_id` | Guarda quem emitiu no modo confidencial | Esquema separado, com chave de criptografia própria. Toda leitura gera `CONSULTA_IDENTIDADE` (RNF-003; ER, seção 10) |
| `Fato.relator_id` | Guarda quem relatou o fato ao gestor | Nunca exibido ao receptor (RF-012) |
| `VersaoFeedback.criada_por` | Guarda o autor de cada versão | Nulo no modo confidencial: o autor fica só em `VinculoConfidencial` (ER, seção 6; I-04) |
| `PlanoAcao.emissor_id` | Guarda o emissor do feedback que originou o plano | Nulo quando o feedback de origem é confidencial. O plano é feito com o gestor direto (`PlanoAcao.gestor_id`), sem revelar o emissor (ERS-D05; I-05) |

No modo **anônimo**, a identidade não é guardada em lugar nenhum (RN-004; ER, seção 10). O campo `RespostaAvaliacao.avaliador_id` fica nulo, e o convite não tem ligação com a resposta (decisão M-04). O modo anônimo só existe nas respostas de avaliação: um feedback nunca é anônimo (ERS-D03).

### 4.5 Colaboradores menores de 18 anos

- O menor é identificado pela `Colaborador.data_nascimento`. A condição de menor é calculada a partir dela, sem atributo próprio, e muda sozinha aos 18 anos (RN-016, decisão M-07).
- Todos os dados de um colaborador menor, e não só a data de nascimento, devem ser tratados no seu melhor interesse e compartilhados apenas no estritamente necessário (RN-016; LGPD, art. 14).
- Um compartilhamento só abrange dados de menores se `CompartilhamentoDados.inclui_menores` for verdadeiro, com justificativa registrada (ER 1.1; I-12).

### 4.6 Resumo dos prazos de retenção

| Dados | Prazo | Ao fim do prazo | Fonte |
|---|---|---|---|
| Feedbacks, avaliações e planos de ação | Enquanto o colaborador estiver na organização e por 5 anos (60 meses) após o desligamento. Configurável | Eliminar ou anonimizar | RN-011, RF-062 (P-05) |
| Qualquer dado com processo judicial em curso | Enquanto durar o bloqueio | Eliminação suspensa | RF-062 |
| Registros de acesso (sistema operado como serviço) | No mínimo 6 meses | Conforme a categoria | RNF-032 |
| Registro de incidente de segurança | No mínimo 5 anos | Conforme a categoria | RF-063 |
| Rascunho de resposta de avaliação | Até o envio da resposta | Apagado | RNF-012; ER, seção 10 |
| Backups | Seguem a categoria do dado | Dado eliminado deixa de existir ao fim da guarda do backup | Especificação Suplementar, DS-09 |
| Cadastro, metas, check-ins, consentimentos, solicitações de titulares, notificações e demais registros de auditoria | Definido pela organização, como controladora, na configuração de cada categoria | Conforme a categoria | RF-054, RF-062; ERS-D10 |

---

## 5. Pontos não confirmados e inconsistências

Esta seção registra os pontos encontrados na versão 1.0. A correção coube ao responsável por cada artefato, pela gestão de mudanças do [processo de requisitos](Processo_Requisitos.md) (seção 9). Na revisão final (#55), todos foram tratados, e a coluna **Tratamento** indica onde.

### 5.1 Pontos não confirmados

| # | Ponto | Situação na versão 1.0 | Afeta | Tratamento |
|---|---|---|---|---|
| G-01 | Tamanhos, formatos, obrigatoriedade e regras marcados com `*` | Propostos por este documento. O ER é conceitual e não define tamanhos (ER, seção 1). Confirmar no projeto físico | Seção 3 | Mantido. Os valores com `*` são propostas para o projeto físico, que não faz parte desta etapa |
| G-02 | Valor mínimo aceito para `min_respondentes` | A RN-005 fixa o padrão 3, configurável. O ponto P-03 diz que 3 é o menor valor que impede descobrir o emissor por exclusão, mas a lista não proíbe valores menores | `ConfiguracaoOrganizacao`, `ModalidadeCiclo`, RN-005 | Resolvido. Mínimo de 3 na RN-005 (lista geral 1.1) e no ER 1.1 (ERS-D08) |
| G-03 | Prazo de retenção do cadastro, das metas, dos check-ins, dos consentimentos, das solicitações de titulares, das notificações e da trilha de auditoria (fora os registros de acesso) | A RN-011 cobre só feedbacks, avaliações e planos de ação | Seção 4.6, RF-062 | Resolvido. A organização define os prazos por categoria (RF-062, ERS-D10) |
| G-04 | Prazos de resposta às solicitações de titular, além dos 15 dias do RF-056 | A regulamentação da ANPD sobre direitos do titular ainda está pendente (pesquisa documental, FD-08) | `SolicitacaoTitular.prazo` | Resolvido. A organização define os prazos, além dos 15 dias do RF-056 (ERS-D10) |
| G-05 | Base legal de cada categoria | Indicada como "provável" na seção 4.2. Quem decide é o controlador (RF-054) | `CategoriaDado.base_legal` | Resolvido. A base legal é registrada pelo controlador em `CategoriaDado.base_legal` (RF-054, ERS-D10) |
| G-06 | Modo de identificação do feedback para colaborador de outra área (`DirecaoFeedback.OUTRA_AREA`) | A RN-004 define o modo do gestor, da avaliação ascendente, dos pares e da equipe, mas não o de outra área | `Feedback.modo_identificacao` | Resolvido. Identificado (ERS-D06, UC08-D04) |
| G-07 | Canal das notificações (no sistema e por e-mail) | Decisão DS-10 da Especificação Suplementar. O ER não guarda o canal | `Notificacao` | Resolvido. Dentro do sistema e por e-mail (DS-10). Os dois canais valem para toda notificação, por isso o ER não precisa guardar o canal |
| G-08 | Responsável deste documento | Não preenchido no cabeçalho | Cabeçalho | Resolvido. Cabeçalho preenchido |

### 5.2 Inconsistências entre o ER e a lista geral

| # | Inconsistência | Onde | Requisitos | Tratamento |
|---|---|---|---|---|
| I-01 | **Perfis sem diretoria nem encarregado.** O enumerado `Perfil` tem só os 4 perfis do RF-003. O Documento Visão (seção 3.3) lista a diretoria e o encarregado de dados como usuários, e o diagrama de casos de uso tem o ator Encarregado (DPO). Sem um perfil, o sistema não tem como dar a eles o acesso que o RNF-001 e o RF-061 preveem | `Perfil`, `PerfilColaborador` | RF-003, RNF-001, RF-061 | Resolvido. RF-003 na lista geral 1.1 e enumeração `Perfil` no ER 1.1 (ERS-D02) |
| I-02 | **Emissor obrigatório e modo anônimo.** A RN-002 exige o emissor em todo feedback. No modo anônimo, o ER não guarda o emissor em lugar nenhum. A lista não registra essa exceção | `Feedback.emissor_id` | RN-002, RN-004 | Resolvido. Feedback nunca é anônimo; o anonimato só existe nas respostas de avaliação (ERS-D03) |
| I-03 | **Edição no modo anônimo.** A RN-003 permite que o emissor edite o feedback. O ER aceita que, no modo anônimo, a resposta não possa ser editada, porque o sistema não sabe quem a escreveu (ER, seção 10). A lista não registra essa exceção | `VersaoFeedback`, `RespostaAvaliacao` | RN-003, RN-004 | Resolvido. A resposta anônima não pode ser alterada depois do envio, e o avaliador é avisado (ERS-D04, UC14-D02) |
| I-04 | **Autor da versão expõe o emissor.** `VersaoFeedback.criada_por` guarda o emissor mesmo nos modos confidencial e anônimo. Isso contradiz a própria seção 10 do ER ("`emissor_id` fica nulo") e o RNF-003 (vínculo guardado à parte). O mesmo vale para o rascunho de feedback (`Feedback.status = RASCUNHO`): com `emissor_id` nulo, não há como saber de quem é o rascunho | `VersaoFeedback.criada_por`, `Feedback.status` | RNF-003, RN-004, RNF-012 | Resolvido no ER 1.1. `criada_por` nulo no modo confidencial; rascunho ligado ao autor até o envio |
| I-05 | **Plano de ação revela o emissor.** O plano é feito em conjunto pelo emissor e pelo receptor (RN-006), e `PlanoAcao.emissor_id` guarda o emissor. Se o feedback construtivo vier de um par, da equipe ou da avaliação ascendente, o modo padrão é confidencial (RN-004), e o plano conjunto revela ao receptor quem emitiu | `PlanoAcao.emissor_id` | RN-004, RN-006, RF-042 | Resolvido. Plano definido pelo receptor e pelo gestor direto (RN-006 na lista geral 1.1, ERS-D05); `PlanoAcao.gestor_id` no ER 1.1 |
| I-06 | **Pesos.** O RF-010 fala em pesos "aos feedbacks de um período e aos indicadores de um mesmo feedback". O ER põe `peso` em `CargoCompetencia`, `Pergunta`, `ModalidadeCiclo` e `Indicador`, mas não em `Feedback`. Os pesos de competência no cargo e de pergunta vão além do texto do requisito | Atributos `peso` | RF-010 | Resolvido no ER 1.1. `Feedback.peso`; pesos adicionais exibidos no cálculo (RN-008) |
| I-07 | **Retenção em dois lugares.** `ConfiguracaoOrganizacao.retencao_pos_desligamento_meses` e `CategoriaDado.prazo_retencao_meses` guardam prazos de retenção. O ER não diz qual vale quando os dois divergem | `ConfiguracaoOrganizacao`, `CategoriaDado` | RN-011, RF-062 | Resolvido no ER 1.1. O prazo da categoria prevalece |
| I-08 | **Meta com dois indicadores de resultado.** `Meta.status` já tem `ATINGIDA` e `NAO_ATINGIDA`, e `Meta.atingida` repete a mesma informação | `Meta` | RF-047 | Resolvido no ER 1.1. `Meta.atingida` removido |
| I-09 | **Enumerações incompletas.** `ResultadoConsolidado.modalidade` usa `AGREGADO`, que não está em `ModalidadeAvaliacao`. `RegistroAuditoria.acao` e `ConfiguracaoCheckIn.frequencia` terminam em "...", sem a lista completa de valores | Seção 3.7 | RN-005, RNF-005, RF-041 | Resolvido no ER 1.1. Enumerações `AcaoAuditoria` e `FrequenciaCheckIn` e domínio de `ResultadoConsolidado.modalidade` |
| I-10 | **Check-in sem ligação com metas e planos.** O RF-041 diz que os check-ins periódicos ficam vinculados às metas e aos planos de ação em andamento. `CheckIn` não tem FK para `Meta` nem para `PlanoAcao`; a ligação só existe indiretamente, pelo colaborador | `CheckIn` | RF-041 | Resolvido no ER 1.1. `CheckInMeta` e `CheckInPlano` |
| I-11 | **Visibilidade ampliada sem destinatários.** O RNF-002 permite ao emissor ampliar a visibilidade. O ER tem o valor `AMPLIADA`, mas não guarda para quem ela foi ampliada | `Feedback.visibilidade` | RNF-002 | Resolvido no ER 1.1. `DestinatarioVisibilidade` |
| I-12 | **Compartilhamento de dados de menores.** A RN-016 manda compartilhar os dados de menores só no estritamente necessário. `CompartilhamentoDados` é definido por categoria de dado e não permite tratar os titulares menores de forma diferente | `CompartilhamentoDados` | RN-016 | Resolvido no ER 1.1. `CompartilhamentoDados.inclui_menores` |
| I-13 | **Dados sem entidade.** O RF-038 (sugerir horários livres) precisa conhecer a agenda das pessoas. A decisão DS-13 (lista de termos ofensivos mantida pelo administrador, RNF-024) e a decisão DS-06 (espera crescente e bloqueio após falhas de login, RNF-006) precisam guardar dados. Nenhum dos três tem entidade ou atributo no ER | ER | RF-038, RNF-024, RNF-006 | Resolvido no ER 1.1. `DisponibilidadeAgenda`, `TermoOfensivo` e controle de falhas de login em `Colaborador` |
| I-14 | **Quem configura o modo de identificação.** O RF-030 dá essa função ao RH ou ao administrador, e este documento usa essa regra em `ModalidadeCiclo.modo_identificacao`. O caso de uso UC-13 inclui o modo de identificação entre as tarefas do gestor | Diagrama de casos de uso, UC-13 | RF-030 | Resolvido. Só o RH ou o administrador altera o modo; o gestor usa o padrão da RN-004 (ERS-D07, UC13-D02) |

### 5.3 Termos usados de forma diferente

| # | Termo | Uso divergente | Proposta para este glossário | Tratamento |
|---|---|---|---|---|
| T-01 | **Modalidade** | A lista geral (seção 2.4) define modalidade como "quem avalia quem". O RF-013, a RN-002 e o atributo `Feedback.modalidade` usam a palavra para "formal ou informal". No ER, "quem avalia quem" é `Feedback.direcao` e `ModalidadeCiclo.modalidade` | Manter "modalidade" para "quem avalia quem", como na seção 2.4. No RF-013, na RN-002 e em `Feedback.modalidade`, ler a palavra como "formal ou informal" | Resolvido. Leitura padronizada na ERS-D09 (1) |
| T-02 | **Check-in** | A lista geral (seção 2.4) chama de check-in o ponto de verificação do ciclo **e** o do plano de ação. No ER, o plano de ação usa `PontoMonitoramento`, e `CheckIn` vale só para ciclo e para check-in periódico | Check-in para o ciclo e o periódico; ponto de monitoramento para o plano, como no ER | Resolvido. Proposta adotada (ERS-D09 (2)) |
| T-03 | **360° e equipe** | O RF-024 lista "de equipe (todos avaliam todos)" e "360°" como modalidades diferentes. A PO descreve o 360° também como "todos avaliam todos" (E01 §14, §21). O ER tem os dois valores e permite ainda combinar modalidades no mesmo ciclo | Na avaliação de equipe, todos os membros avaliam todos (RF-024). No 360°, o gestor seleciona ou convida os participantes, que precisam ser do seu time (RF-025) | Resolvido. Diferença tirada do texto do RF-024 e do RF-025 (ERS-D09 (3)) |
| T-04 | **Avaliador, participante convidado, emissor** | O ER usa `avaliador_id`; o RF-027 fala em "participante convidado"; o diagrama de casos de uso usa o ator "Avaliador convidado"; a lista geral (seção 2.4) usa "emissor" também para quem responde a uma avaliação | "Emissor" como termo geral; "avaliador convidado" para o papel no ciclo | Resolvido. Proposta adotada (ERS-D09 (4)) |
| T-05 | **Receptor e avaliado** | A lista geral usa "receptor"; o ER usa `avaliado_id` nas entidades de ciclo | "Receptor" no feedback; "avaliado" no ciclo, como sinônimos | Resolvido. Proposta adotada (ERS-D09 (5)) |
| T-06 | **Ciclo** | "Ciclo de feedback formal" (RF-022), "ciclo formal" (seção 2.4) e "ciclo de avaliação" (ER, casos de uso) | "Ciclo de avaliação", com os outros como sinônimos | Resolvido. Proposta adotada (ERS-D09 (6)) |
| T-07 | **Encarregado** | "Encarregado" (RF-053), "encarregado de dados da organização" (RF-061), "Encarregado de dados (DPO)" (casos de uso) | "Encarregado", com "encarregado de dados" e "DPO" como sinônimos | Resolvido. Proposta adotada (ERS-D09 (7)) |
| T-08 | **Nome do sistema** | Na versão 1.0, a lista geral, a Especificação Suplementar e o diagrama de casos de uso usavam "Sistema de Gestão de Competências (módulo de Feedback)". O Documento Visão e o ER usavam "Sistema Web de Feedback e Gestão de Competências" | Este documento usa o nome do Documento Visão, padronizado nos demais | Resolvido. Nome do Documento Visão adotado (ERS-D01) e padronizado nos cabeçalhos dos artefatos na revisão final |

---

## 6. Fontes

| Fonte | Artefato | Issue |
|---|---|---|
| Requisitos consolidados | [Lista Geral de Requisitos](Lista_Geral_Requisitos.md) e [CSV](Lista_Geral_Requisitos.csv) | #45 |
| Modelo de dados | [Modelo de Domínio e ER](modelagem/modelo-dados/Modelo_Dominio_ER.md) | #52 |
| Visão do produto | [Documento Visão](Documento_Visao.md) | #46 |
| Requisitos não funcionais | [Especificação Suplementar](Especificacao_Suplementar.md) | #51 |
| Casos de uso | [Diagrama de Casos de Uso](modelagem/casos-de-uso/Diagrama_Casos_de_Uso.md) | #47 |
| Entrevistas (E01 e E02) | [Síntese dos Requisitos das Entrevistas](elicitacao/entrevistas/Sintese_Requisitos_Entrevistas.md) | #41 |
| Questionários (Q01 e Q02) | [Síntese dos Requisitos dos Questionários](elicitacao/questionarios/Sintese.md) | #42 |
| Pesquisa documental (LGPD) | [Pesquisa Documental](elicitacao/pesquisa-documental/Pesquisa_Documental.md) | #33 |
| Sistema análogo (15Five) | [Síntese dos Requisitos do Sistema Análogo](elicitacao/sistema-analogo/Sintese_Requisitos_Sistema_Analogo.md) | #43 |
| Processo atual (AS-IS 1 e 2) | [Processo AS-IS de feedback e avaliação, com as dores](elicitacao/bpmn/Processo_AS-IS_e_Dores.md) | #44 |
| Método | LARMAN, C. *Utilizando UML e Padrões*, cap. 7 | - |
| Legislação | Lei nº 13.709/2018 (LGPD), arts. 5º, 12, 13, 14, 18, 38, 41 e 48 | - |
