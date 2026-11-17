# UC-08 Registrar feedback

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Formato:** completo (Larman, cap. 6) · **Issue:** #48 · **Versão:** 1.0 · **Data:** 17/11/2026
**Responsável:** Davi Augusto Ferreira de Carvalho
**Prioridade:** Must · **Área:** Feedback do dia a dia · [Diagrama](Diagrama_Casos_de_Uso.md#42-feedback-do-dia-a-dia) · [Modelo e convenções](Casos_de_Uso_Completos.md)

---

## 1. Escopo

Sistema Web de Feedback e Gestão de Competências.

## 2. Nível

Objetivo do usuário.

## 3. Ator principal

**Colaborador, no papel de emissor**: quem dá o feedback. Na maioria dos casos é o gestor, para um colaborador da sua equipe. Também pode ser um colaborador que dá feedback a alguém de outra área ou que atende ao pedido de um colega (UC-09) (diagrama, seção 2; E01 §10).

## 4. Interessados e interesses

| Interessado | Interesse |
|---|---|
| **Emissor** | Registrar rápido, sem "ficar horas preenchendo informações" (E02 §8): o feedback informal cabe em uma única tela (RNF-013). Ter apoio para escrever, porque "gestores não sabem dar feedback" foi o problema citado nos dois questionários (RF-016, RF-017). Não perder o que já escreveu (RNF-012). Saber, antes de enviar, quem verá o conteúdo e a sua identidade (RF-019). Poder corrigir um texto mal escrito sem apagar o registro (RN-003; E01 §20) |
| **Receptor** (colaborador ou membros da equipe) | Receber um feedback baseado em fatos e comportamentos observados, e não em opinião ou traços de personalidade (RN-001; E01 §20). Ter o feedback no próprio histórico, para acompanhar a sua evolução (RF-048). Saber quem emitiu, quando o feedback é identificado (E01 §11). Poder registrar uma réplica sem alterar o texto do emissor (RF-020) |
| **Gestor direto do receptor** | Ver os feedbacks recebidos pelos colaboradores da sua equipe, inclusive os dados por pessoas de outras áreas (RNF-001; E01 §10) |
| **RH** | Ter "esse controle" dos feedbacks que estão sendo dados (E01 §10). Contar com um registro oficial, que não pode ser excluído, para o histórico e para o resguardo jurídico da organização (RN-003; E01 §20, §32). Conseguir consultar a identidade do emissor de feedbacks confidenciais (RN-004) |
| **Colega que relatou um fato** | Não ter a identidade revelada ao receptor quando o fato vem de um relato (RF-012; E02 §3) |
| **Organização contratante** | Cumprir a LGPD: coletar só o necessário, sem dados sensíveis (RN-013, RF-018), informar com clareza quem vê o quê (art. 6º, VI) e manter a trilha de auditoria (RNF-005) |

## 5. Pré-condições

1. O Emissor está autenticado (RF-003).
2. O receptor, colaborador ou equipe, está cadastrado e ativo (UC-01).
3. No feedback formal, há um ciclo aberto, planejado no UC-13, em que o receptor é avaliado e o Emissor é o responsável pelo feedback (RF-022).

## 6. Garantia de sucesso (pós-condições)

1. O feedback foi gravado como enviado, com emissor, receptor, data, tipo, modalidade e pelo menos um fato vinculado (RN-002). O conteúdo está na versão 1 (RN-003, M-03).
2. A identidade do emissor foi gravada de acordo com o modo de identificação (RN-004): junto ao feedback, se identificado; só no vínculo separado, acessível ao RH, se confidencial (RNF-003).
3. Os fatos vinculados deixaram de ser privados de quem os registrou e passaram a seguir a visibilidade do feedback (RF-011).
4. As competências tratadas no feedback estão vinculadas a ele (RF-021).
5. O feedback está visível apenas ao público mínimo: receptor, emissor, gestor direto do receptor e RH (RNF-001, RNF-002).
6. O feedback consta no histórico do receptor (RF-048). Se o receptor é uma equipe, o Sistema guardou quem era membro na data do feedback, e o feedback aparece no histórico de cada um deles, sinalizado como "feedback em grupo" (M-09).
7. O receptor foi avisado dentro do sistema (UC08-D01).
8. A criação foi registrada na trilha de auditoria (RNF-005), e o rascunho deixou de existir.

## 7. Cenário de sucesso principal

O cenário descreve o caso mais comum: o gestor registra um feedback informal para um colaborador da sua equipe.

1. O Emissor pede para registrar um feedback.
2. O Sistema pede o receptor, o tipo (positivo ou construtivo), a modalidade (formal ou informal) e a data do feedback (RF-013).
3. O Emissor informa o receptor, o tipo, a modalidade informal e a data.
4. O Sistema identifica a direção do feedback pela hierarquia, neste caso gestor → colaborador, e o modo de identificação correspondente, neste caso identificado (RN-004; UC08-D04). Apresenta a estrutura do tipo escolhido, com orientações e exemplos (RF-016, RF-017), e os fatos que o Emissor já registrou sobre o receptor e ainda não vinculou a um feedback (RF-011).
5. O Emissor escolhe um ou mais fatos que fundamentam o feedback (RN-001, RN-002).
6. O Emissor preenche a estrutura do tipo e escolhe as competências do receptor tratadas no feedback (RF-016, RF-021):
   - **positivo**: a ação ou o comportamento, os resultados e a repercussão para o gestor, o time e a organização;
   - **construtivo**: um aspecto positivo, o problema associado aos fatos, a repercussão e a reflexão feita com o receptor.
7. O Sistema salva o feedback como rascunho enquanto o Emissor preenche (RNF-012).
8. O Emissor pede para enviar o feedback.
9. O Sistema confere os campos obrigatórios e pede a confirmação do envio, informando em linguagem clara quem poderá ver o conteúdo e a identidade do Emissor (RN-002, RF-019, RNF-015).
10. O Emissor confirma o envio.
11. O Sistema grava o feedback como enviado, na versão 1, com os fatos e as competências vinculados, e registra a criação na trilha de auditoria (RN-003, RNF-002, RNF-005).
12. O Sistema confirma o registro ao Emissor e avisa o receptor de que há um novo feedback no seu histórico (RF-048; UC08-D01).

## 8. Extensões

**\*a. A qualquer momento, o Emissor interrompe o preenchimento ou a sessão expira.**

1. O Sistema mantém o rascunho salvo (RNF-012). A sessão expira após 1 h sem atividade (RNF-006, DS-05).
2. Quando o Emissor volta, o Sistema apresenta os seus rascunhos, e o cenário continua no passo em que ele parou.

**1a. O Emissor registra o feedback para atender a uma solicitação de um colega (UC-09).**

1. O Emissor escolhe a solicitação pendente.
2. O Sistema preenche o solicitante como receptor e apresenta o tema e o prazo da solicitação (RF-031).
3. O cenário continua no passo 4, com a direção entre pares. Ao gravar, no passo 11, o Sistema marca a solicitação como atendida para o Emissor.

**3a. O receptor é uma equipe.**

1. O Sistema apresenta os membros da equipe na data do feedback e informa que o feedback aparecerá no histórico de cada um deles como "feedback em grupo" (M-09).
2. O cenário continua no passo 4, e o Sistema apresenta os fatos registrados sobre a equipe ou sobre os seus membros (UC08-D02).
3. Ao gravar, no passo 11, o Sistema guarda a lista de membros daquela data. Quem entrar na equipe depois não recebe o feedback, e quem sair continua com ele no histórico.

**3b. A modalidade é formal.**

1. O Sistema pede o ciclo e lista os ciclos abertos em que o receptor é avaliado e o Emissor é o responsável (RF-022).
2. O Emissor escolhe o ciclo.
3. O Sistema apresenta os objetivos, as competências e os indicadores do ciclo, com os valores registrados nos check-ins (RF-023), para que o feedback se baseie nos parâmetros planejados: "dou o feedback daquela pessoa em relação àqueles parâmetros que foram estabelecidos no planejamento" (E01 §17).
4. O cenário continua no passo 4. Ao gravar, o Sistema vincula o feedback ao ciclo.

**3c. O receptor é de outra área, e não da equipe do Emissor.**

1. O Sistema registra a direção "outra área", com modo identificado (RN-004; E01 §10).
2. O cenário continua no passo 4. No passo 9, o Sistema informa também que o gestor direto do receptor poderá ver o feedback (RNF-001).

**3d. O Emissor escolhe o reconhecimento rápido: feedback positivo e informal.**

1. O Sistema apresenta o formulário simplificado, em uma única tela, só com os campos obrigatórios de RN-002 (RF-015, RNF-013). O fato continua obrigatório.
2. O Emissor escolhe ou registra o fato e descreve o reconhecimento.
3. O cenário continua no passo 8.

**3e. A data informada é posterior à data atual.**

1. O Sistema informa que a data do feedback não pode estar no futuro (UC08-D05).
2. O cenário volta ao passo 3.

**4a. O Emissor não tem fatos registrados sobre o receptor que ainda não estejam vinculados.**

1. O Sistema informa que não há fatos disponíveis e oferece o registro de um fato nesse momento.
2. O Emissor registra o fato, com data e descrição, da mesma forma que no UC-06 (RF-011).
3. O cenário continua no passo 5.

**5a. Um dos fatos escolhidos é um relato de colega ainda não confirmado.**

1. O Sistema informa que um relato só pode embasar um feedback depois de confirmado pela observação do próprio Emissor (RF-012; P-06).
2. O Emissor confirma que verificou o fato pessoalmente, e o cenário continua no passo 6, **ou** retira o relato, e o cenário volta ao passo 5.

**6a. O Emissor preenche um campo de texto livre.**

1. O Sistema orienta a descrever fatos e comportamentos observáveis e a não incluir dados sensíveis, informações de saúde ou dados de terceiros (RF-018).
2. O cenário continua no passo 6.

**9a. Falta um campo obrigatório: receptor, tipo, modalidade, data ou pelo menos um fato.**

1. O Sistema identifica cada campo com problema e sugere a correção (RN-002, RNF-021).
2. O cenário volta ao passo 5.

**9b. Um texto livre contém termo da lista de termos ofensivos ou discriminatórios mantida pelo administrador (Could).**

1. O Sistema destaca o trecho e sugere a revisão, sem bloquear o envio (RNF-024, DS-13).
2. O Emissor revisa o texto, e o cenário volta ao passo 6, **ou** mantém o texto, e o cenário continua no passo 10.

**10a. O Emissor não confirma o envio.**

1. O Sistema mantém o feedback como rascunho.
2. O cenário volta ao passo 6.

**11a. O Sistema não consegue concluir o envio.**

1. O Sistema informa que o feedback não foi enviado e mantém o rascunho.
2. O cenário volta ao passo 8.

**12a. O feedback é construtivo.**

1. O Sistema oferece a criação do plano de ação, que é construído em conjunto pelo emissor e pelo receptor (RF-042, RN-006).
2. O Emissor cria o plano agora, e começa o UC-19 (ponto de extensão do diagrama), **ou** deixa para a sessão de feedback, e o caso de uso termina.

**12b. O Emissor quer marcar a conversa com o receptor para comunicar o feedback.**

1. O Emissor pede para agendar a sessão a partir do feedback.
2. Começa o UC-11, com o feedback já vinculado à sessão (RF-037).

**12c. Depois do envio, o Emissor quer corrigir o feedback.**

1. O Emissor escolhe um feedback que ele enviou.
2. O Sistema apresenta a versão vigente para edição. Não há opção de excluir o feedback (RN-003; E01 §20).
3. O Emissor altera o conteúdo e confirma.
4. O Sistema grava uma nova versão datada, mantém a anterior e registra a alteração na trilha de auditoria (RN-003, RNF-005; P-04).
5. O Sistema avisa o receptor de que o feedback foi editado (UC08-D03).
6. O caso de uso termina.

## 9. Requisitos especiais

| Requisito | Como se aplica a este caso de uso |
|---|---|
| Rapidez de registro | O feedback informal cabe em uma única tela, só com os campos obrigatórios de RN-002 (RNF-013) |
| Tempo de resposta | O formulário de feedback carrega em até 3 s e o envio é confirmado em até 2 s, no percentil 95, em conexão 4G (RNF-008, DS-02) |
| Rascunho automático | Nada do que foi preenchido se perde com queda de conexão, sessão expirada ou campo obrigatório em branco (RNF-012) |
| Visibilidade mínima | Só receptor, emissor, gestor direto do receptor e RH veem o feedback. A visibilidade é definida no envio e só pode ser ampliada por nova ação do emissor (RNF-001, RNF-002) |
| Identidade do emissor confidencial | No modo confidencial, o vínculo entre emissor e feedback fica separado do conteúdo, e toda consulta do RH vai para a auditoria (RNF-003; modelo ER, seção 10) |
| Segurança e auditoria | Conteúdo criptografado em trânsito e em repouso (RNF-004). Criação, edição e consulta registradas na trilha de auditoria (RNF-005) |
| Proteção contra erro | Pedir confirmação antes do envio e indicar o erro com sugestão de correção (RNF-015, RNF-021) |
| Idioma, acessibilidade e responsividade | Interface e orientações em português do Brasil (RNF-016). ABNT NBR 17225:2025 e WCAG 2.2 A e AA (RNF-017 a RNF-023). Uso em computador e celular (RNF-027) |

## 10. Lista de variações de tecnologia e dados

1. **Tipo:** positivo ou construtivo, cada um com a sua estrutura (RF-016). O reconhecimento rápido usa o formulário simplificado (RF-015).
2. **Modalidade:** informal, a qualquer momento (RF-014), ou formal, vinculada a um ciclo (RF-022).
3. **Receptor:** um colaborador ou uma equipe (RF-013; M-09).
4. **Momento do registro:** antes da conversa com o receptor ou depois dela. A data do feedback pode ser anterior à data do registro (UC08-D05).
5. **Aviso ao receptor:** dentro do sistema (DS-10; UC08-D01).
6. **Uso por navegador** em computador ou celular: Chrome, Edge, Firefox e Safari, na versão atual e na anterior (RNF-030, DS-07).

## 11. Frequência de ocorrência

É o caso de uso mais frequente do sistema. O feedback informal é dado sob demanda, sempre que o emissor observa algo a corrigir ou a reconhecer (E01 §3, §12). Na E02, a secretária chama para conversar o servidor que "com frequência" perde prazos, e os feedbacks que ela mais dá são os construtivos (E02 §2). O feedback formal acontece ao fim de cada ciclo, que a PO citou como de 3 ou 4 meses (E01 §5), uma vez por avaliado.

## 12. Decisões de especificação

| # | Questão | Decisão | Justificativa |
|---|---|---|---|
| UC08-D01 | O receptor é avisado quando recebe um feedback? | Sim, por aviso dentro do sistema, ao enviar e ao editar. **Impacto no modelo ER (#52), aplicado na versão 1.1 do modelo:** acrescentar o valor `FEEDBACK_RECEBIDO` à enumeração `TipoNotificacao` | Sem aviso, o reconhecimento rápido (RF-015) não chegaria a quem foi reconhecido, e ele substitui a mensagem de WhatsApp que a E02 usa hoje (E02 §2). O canal segue a DS-10. O aviso não leva o conteúdo, só indica que há um feedback novo no histórico (RNF-002) |
| UC08-D02 | Como registrar fatos sobre uma equipe, se `Fato` só tem um colaborador observado (`observado_id`)? | O feedback para equipe aceita fatos de qualquer membro. **Impacto no modelo ER (#52), aplicado na versão 1.1 do modelo:** acrescentar `observado_equipe_id` a `Fato`, para fatos sobre a equipe como um todo, como "o time atrasou as entregas do mês" | RN-002 exige pelo menos um fato em todo feedback, e RN-001 exige que o fato seja sobre o receptor. Sem o campo, um feedback para a equipe teria de usar fatos de uma pessoa só, o que mistura problema individual com problema do grupo |
| UC08-D03 | O receptor vê as versões anteriores de um feedback editado? | Sim. O receptor e o RH veem a versão vigente, com a indicação de que foi editada, e podem consultar as anteriores | O feedback é registro oficial (E01 §20). Se o receptor já registrou uma réplica sobre a versão anterior (RF-020), uma edição silenciosa mudaria o sentido da réplica. RN-003 guarda as versões, e esta decisão define quem as vê |
| UC08-D04 | Qual o modo de identificação de um feedback dado fora de um ciclo? | Segue o padrão de RN-004 pela direção: gestor → colaborador e outra área, **identificado**; entre pares e ascendente, **confidencial**. O modo anônimo só existe em ciclos | RF-030 configura o modo por ciclo e modalidade, então fora de um ciclo vale o padrão de RN-004. Se a solicitação de feedback (UC-09) tiver um único destinatário, o aviso do passo 9 lembra que o solicitante pode deduzir quem respondeu (RF-019) |
| UC08-D05 | A data do feedback pode ser diferente da data do registro? | Sim, pode ser anterior, mas não futura | A conversa costuma acontecer antes do registro: a PO comunica o feedback e depois registra (E01 §1), e a E02 conversa no fim do expediente (E02 §2). Uma data futura não descreve um feedback já dado. Para marcar uma conversa futura existe o UC-11 |

## 13. Rastreabilidade

| Tipo | Itens |
|---|---|
| Requisitos funcionais | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-021 (do diagrama); RF-011, RF-012, RF-020, RF-022, RF-023, RF-031, RF-037, RF-042, RF-048 (relacionados) |
| Requisitos não funcionais | RNF-001, RNF-002, RNF-003, RNF-004, RNF-005, RNF-006, RNF-008, RNF-012, RNF-013, RNF-015, RNF-016, RNF-017 a RNF-023, RNF-024, RNF-027, RNF-030 |
| Regras de negócio | RN-001, RN-002, RN-003, RN-004, RN-006, RN-013 |
| Entidades do modelo ER | `Feedback`, `VersaoFeedback`, `FeedbackFato`, `Fato`, `FeedbackCompetencia`, `MembroFeedbackEquipe`, `VinculoConfidencial`, `SolicitacaoFeedback`, `DestinatarioSolicitacao`, `Notificacao`, `RegistroAuditoria` |
| Casos de uso relacionados | UC-06 (registro de fato), UC-07 (relato de colega), UC-09 (solicitação de feedback), UC-10 (réplica do receptor), UC-11 (agendamento da sessão), UC-13 (ciclo formal), UC-19 (plano de ação, extensão), UC-22 (histórico do receptor) |
| Decisões aplicadas | P-01, P-04, P-06 (lista geral); DS-02, DS-05, DS-07, DS-10, DS-13 (especificação suplementar); M-03, M-09 (modelo ER) |
| Fontes | [Entrevista 01](../../elicitacao/entrevistas/Entrevista01_Adriana.md), §1, §2, §3, §10, §11, §12, §16, §17, §20 e §32; [Entrevista 02](../../elicitacao/entrevistas/Entrevista02_Eliene.md), §2, §3 e §8; [Síntese dos questionários](../../elicitacao/questionarios/Sintese.md); [Processo AS-IS e dores](../../elicitacao/bpmn/Processo_AS-IS_e_Dores.md) |
