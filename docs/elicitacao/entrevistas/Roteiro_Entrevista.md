# Roteiro de Entrevista – Feedback e Gestão de Competências

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software — Bacharelado em Engenharia de Software — Universidade Federal de Goiás (UFG)
**Técnica de elicitação:** Entrevista semiestruturada
**Duração prevista:** 45 a 60 minutos
**Versão reduzida (20 a 25 min):** [Roteiro_Entrevista_Reduzido.md](Roteiro_Entrevista_Reduzido.md)
**Termo de consentimento:** [Termo_Consentimento_Entrevista.md](Termo_Consentimento_Entrevista.md)

---

## Sumário

1. [Objetivo do roteiro](#1-objetivo-do-roteiro)
2. [Perfis de entrevistados](#2-perfis-de-entrevistados)
3. [Orientações ao entrevistador](#3-orientações-ao-entrevistador)
4. [Abertura e consentimento](#4-abertura-e-consentimento)
5. [Identificação do entrevistado](#5-identificação-do-entrevistado)
6. [Blocos de perguntas](#6-blocos-de-perguntas)
   - [Bloco A – Contexto e processo atual](#bloco-a--contexto-e-processo-atual)
   - [Bloco B – Tipos de feedback: chefe-colaborador, pares e 360º](#bloco-b--tipos-de-feedback-chefe-colaborador-pares-e-360º)
   - [Bloco C – Feedback formal, informal, positivo e construtivo](#bloco-c--feedback-formal-informal-positivo-e-construtivo)
   - [Bloco D – Uso de questionários na avaliação](#bloco-d--uso-de-questionários-na-avaliação)
   - [Bloco E – Análise, indicadores e visualizações](#bloco-e--análise-indicadores-e-visualizações)
   - [Bloco F – Confidencialidade e anonimato](#bloco-f--confidencialidade-e-anonimato)
   - [Bloco G – Acompanhamento, plano de ação e histórico](#bloco-g--acompanhamento-plano-de-ação-e-histórico)
   - [Bloco H – Metas e plano de desenvolvimento](#bloco-h--metas-e-plano-de-desenvolvimento)
   - [Bloco I – Principais dores do processo atual (alimenta o BPMN)](#bloco-i--principais-dores-do-processo-atual-alimenta-o-bpmn)
7. [Encerramento](#7-encerramento)
8. [Checklist pós-entrevista](#8-checklist-pós-entrevista)
9. [Matriz de cobertura do escopo](#9-matriz-de-cobertura-do-escopo)

---

## 1. Objetivo do roteiro

Padronizar as entrevistas de levantamento de requisitos para que todas cubram o escopo definido pela Product Owner e permitam comparar as respostas entre entrevistados. O roteiro é **semiestruturado**: as perguntas principais devem ser feitas a todos; as perguntas de aprofundamento (marcadas com ↳) são opcionais e dependem do que o entrevistado trouxer.

O roteiro foi elaborado a partir do escopo do projeto (README), da [Entrevista 01 com a Profa. Adriana](Entrevista01_Adriana.md) e dos resultados do [Questionário 01](../questionarios/Questionario01_Isabella.md), de forma a aprofundar os pontos que ainda estão em aberto, em especial a tensão sobre anonimato, o ciclo formal de avaliação e as dores do processo atual.

## 2. Perfis de entrevistados

Conforme orientação da Product Owner (Entrevista 01, seções 28 e 34), devem ser priorizados perfis que **dão** ou **administram** feedback. Cada entrevista deve, preferencialmente, ter um perfil diferente da anterior.

| Perfil | O que se espera descobrir | Blocos prioritários |
|---|---|---|
| **Gestor / líder de equipe** | Como planeja, registra e acompanha o feedback dos liderados; que instrumentos usa (planilha, ferramenta, papel). | A, B, C, G, H, I |
| **RH / Gestão de Pessoas** | Como o ciclo de avaliação é conduzido na organização; consolidação de resultados; relatórios; controle de acesso; retenção de dados. | A, D, E, F, I |
| **Colaborador sem liderança** | Como recebe feedback; percepção sobre sinceridade, anonimato e utilidade; o que gostaria de acompanhar sobre si. | B, C, F, G, H |

Se o entrevistado acumular papéis (por exemplo, gestor que também é avaliado pelo chefe), percorrer os dois conjuntos de blocos.

## 3. Orientações ao entrevistador

- **Antes:** ler este roteiro inteiro, revisar a Entrevista 01 e os questionários já respondidos, preparar o termo de consentimento e testar a gravação.
- **Perguntas abertas primeiro.** Deixar o entrevistado descrever o processo com as próprias palavras antes de citar funcionalidades. Evitar perguntas que induzam a resposta ("você não acha que seria bom ter X?").
- **Pedir exemplos e fatos.** Sempre que o entrevistado generalizar ("o feedback aqui é ruim"), pedir um caso concreto: quem, quando, como foi registrado, o que aconteceu depois.
- **Anotar o vocabulário do entrevistado.** Termos como "ciclo", "check-in", "PDI", "avaliação", "devolutiva" devem ir para o glossário (issue #53).
- **Mapear o fluxo para o BPMN.** Nas perguntas do Bloco A e do Bloco I, anotar explicitamente: quem inicia, quem participa, quais artefatos circulam, onde o processo trava.
- **Controlar o tempo.** Tempo sugerido por bloco está indicado no título de cada bloco. Se faltar tempo, priorizar os blocos marcados para o perfil do entrevistado.
- **Divisão de papéis:** um integrante conduz, outro anota e controla o tempo, um terceiro cuida da gravação e observa pontos a aprofundar.

## 4. Abertura e consentimento

*Tempo sugerido: 5 min*

Texto de referência para o entrevistador:

> Olá, obrigado(a) por aceitar participar. Somos alunos da disciplina de Domínios de Software da UFG e estamos levantando requisitos para um sistema web de feedback e gestão de competências. O objetivo desta conversa é entender como o feedback e a avaliação de desempenho acontecem hoje na sua organização, o que funciona e o que não funciona. Não existem respostas certas ou erradas.
>
> A entrevista deve durar cerca de 45 a 60 minutos. Com a sua autorização, vamos gravar o áudio para transcrever depois. A transcrição e os seus dados de identificação (nome, função e telefone) serão usados apenas nesta disciplina e guardados em repositório privado do grupo. Você pode pular qualquer pergunta, interromper a entrevista ou pedir a exclusão dos seus dados a qualquer momento.
>
> Você está de acordo e autoriza a gravação?

- [ ] Ler ou entregar o [Termo de Consentimento](Termo_Consentimento_Entrevista.md).
- [ ] Registrar o aceite (assinatura, "de acordo" por escrito ou verbal gravado).
- [ ] Só iniciar a gravação após o aceite.

## 5. Identificação do entrevistado

*Tempo sugerido: 3 min*

| Campo | Resposta |
|---|---|
| Nome completo | |
| Função / cargo | |
| Telefone | |
| Organização (nome ou segmento) | |
| Porte da organização (nº aproximado de colaboradores) | |
| Tempo na função | |
| Papel no processo de avaliação (dá feedback, recebe, administra o ciclo) | |
| Tamanho da equipe que lidera ou da qual faz parte | |
| Data da entrevista | |
| Entrevistadores | |

## 6. Blocos de perguntas

### Bloco A – Contexto e processo atual

*Tempo sugerido: 8 min · Alimenta o BPMN AS-IS (issue #44)*

1. Conte como funciona o feedback e a avaliação de desempenho na sua organização hoje. Quem participa, com que frequência e como começa?
2. Existe um processo formal definido (política, ciclo de avaliação, calendário)? Quem é o responsável por conduzir esse processo?
3. Que instrumentos vocês usam para registrar feedback e avaliações? (planilha, formulário, sistema de RH, e-mail, papel, nada)
   - ↳ Se usa ferramenta: qual? O que ela faz bem e o que falta?
   - ↳ Se não usa: onde ficam as informações? Elas se perdem?
4. Descreva, passo a passo, o que acontece desde que um gestor decide dar um feedback até o encerramento desse feedback.
5. Existe algum treinamento ou orientação sobre como dar e receber feedback? Como as pessoas reagem quando são chamadas para uma sessão de feedback?

### Bloco B – Tipos de feedback: chefe-colaborador, pares e 360º

*Tempo sugerido: 7 min*

6. Quais destas modalidades acontecem na sua organização: gestor → colaborador, colaborador → gestor, entre pares, avaliação 360º, autoavaliação? Como cada uma funciona?
7. Na avaliação entre pares e na 360º, quem decide quem avalia quem? O gestor escolhe os participantes, todos do time avaliam todos, ou o próprio colaborador indica?
8. Você já fez autoavaliação? Ela é comparada com a percepção dos colegas ou do gestor? Isso foi útil?
9. O que acontece quando alguém convidado a avaliar não responde? Isso é registrado? Há alguma consequência?
10. Acontece feedback entre pessoas de áreas ou times diferentes? Em que situações?

### Bloco C – Feedback formal, informal, positivo e construtivo

*Tempo sugerido: 8 min*

11. Como você diferencia feedback formal de informal no seu dia a dia? O informal é registrado em algum lugar?
12. Quando você dá (ou recebe) um feedback positivo, como ele é estruturado? Ele costuma citar os fatos que motivaram o reconhecimento e o impacto para o time?
13. E o feedback construtivo? Como ele é conduzido? Existe algum roteiro (abrir com ponto positivo, apresentar fatos, refletir junto, combinar plano de ação)?
14. Os feedbacks são baseados em fatos observados ou em impressões gerais? Dê um exemplo recente.
15. Na sua experiência, as pessoas dão mais feedback positivo ou construtivo? Por quê?
16. Um feedback já registrado pode ser editado ou excluído? Quem pode fazer isso? Já houve problema por causa disso?
17. Depois da sessão de feedback, alguém avalia como foi a sessão (postura de quem deu, utilidade para quem recebeu)?

### Bloco D – Uso de questionários na avaliação

*Tempo sugerido: 6 min*

18. A avaliação usa um formulário ou questionário? Quem elabora as perguntas? Elas mudam a cada ciclo?
19. As perguntas são as mesmas para todos ou variam por cargo, por equipe ou por pessoa? Existem competências fixas por cargo e competências específicas por colaborador?
20. Que tipos de pergunta funcionam melhor: escala numérica, escala do tipo "concordo / discordo", texto livre, nota de 0 a 10? Por quê?
21. Faz sentido alguma pergunta ou competência ter peso maior que outra? Em que situação?
22. Quanto tempo uma pessoa leva (ou deveria levar) para responder uma avaliação sobre um colega? A partir de quanto tempo ela deixa de responder com atenção?
23. Seria útil reaproveitar um conjunto de perguntas ou indicadores de um ciclo para o próximo?

### Bloco E – Análise, indicadores e visualizações

*Tempo sugerido: 6 min*

24. Quais indicadores você acompanha (ou gostaria de acompanhar) sobre uma pessoa ou sobre a equipe? Como traduz uma competência ampla, como "comunicação" ou "comprometimento", em algo mensurável?
25. Hoje, como você consolida os resultados de um ciclo de avaliação? Quanto tempo isso leva? Que relatórios são gerados e para quem?
26. Que gráficos ou visualizações seriam mais úteis para você? (evolução ao longo do tempo, comparação entre ciclos, pontos fortes e a melhorar, comparação autoavaliação × avaliação dos outros, andamento das metas)
27. Para o RH ou para a liderança: que visão consolidada da organização ou de um setor seria útil? (por exemplo, quantos feedbacks foram dados, quais planos de ação estão atrasados, quais colaboradores não participaram)
28. Os resultados da avaliação são usados para decisões de promoção ou salário, ou apenas para desenvolvimento? O que deveria ser?

### Bloco F – Confidencialidade e anonimato

*Tempo sugerido: 7 min · Relacionado à pesquisa documental sobre LGPD (issue #33)*

29. Hoje, quem consegue ver os feedbacks e avaliações de uma pessoa? (a própria pessoa, o gestor direto, o RH, a diretoria, os colegas)
30. Quem deveria ver, na sua opinião? Existe alguma informação que deveria ficar restrita?
31. O colaborador sabe quem escreveu cada feedback sobre ele? Em quais modalidades (gestor → colaborador, pares, 360º, colaborador → gestor) o anonimato faz sentido e em quais atrapalha?
32. Você se sentiria à vontade para dar um feedback sincero ao seu gestor se ele soubesse que foi você? E se fosse anônimo? Já viu alguém ser prejudicado por um feedback que deu?
33. Se o RH ou um administrador do sistema consegue identificar o autor de um feedback anônimo, isso quebra a confiança? Como isso deveria ser tratado?
34. Por quanto tempo os feedbacks devem ficar guardados? O que deve acontecer com o histórico quando a pessoa sai da organização?
35. Os colaboradores são informados sobre como seus dados de avaliação são usados? Existe algum consentimento formal?

### Bloco G – Acompanhamento, plano de ação e histórico

*Tempo sugerido: 6 min*

36. Depois de um feedback construtivo, o que acontece? É criado um plano de ação? Quem o elabora: o gestor, o colaborador ou os dois juntos?
37. Como o plano de ação é acompanhado? Existem pontos de verificação (check-ins)? Com que frequência? Quem registra o andamento?
38. O que acontece quando o prazo do plano de ação termina? Como se verifica se a pessoa melhorou?
39. Existe um histórico de todos os feedbacks que uma pessoa recebeu? Onde ele fica? Alguém o consulta na prática? Para quê?
40. Seria útil o sistema enviar lembretes (sessão agendada, check-in pendente, avaliação não respondida)? Para quem?

### Bloco H – Metas e plano de desenvolvimento

*Tempo sugerido: 6 min*

41. No ciclo formal, são definidos objetivos ou metas de desenvolvimento para o colaborador no início do período? Quem define: o gestor, o colaborador, os dois ou o RH?
42. As metas são por pessoa, por cargo ou por equipe? Como são adaptadas para quem precisa de algo específico?
43. Como se mede se uma meta foi atingida? É binário (atingiu / não atingiu) ou existe gradação?
44. Com que periodicidade o ciclo formal acontece (trimestral, semestral, anual)? Essa periodicidade é adequada?
45. Como a evolução da pessoa ao longo de vários ciclos é acompanhada? Você consegue ver se ela está melhorando?

### Bloco I – Principais dores do processo atual (alimenta o BPMN)

*Tempo sugerido: 8 min · Alimenta as dores do BPMN AS-IS (issue #44)*

46. Quais são as três maiores dificuldades do processo de feedback e avaliação hoje?
47. Em que etapa do processo as coisas mais travam ou se perdem? (planejar, coletar fatos, agendar a sessão, registrar, acompanhar o plano de ação, consolidar resultados)
48. O que faz as pessoas deixarem de dar ou registrar feedback? (falta de tempo, de instrumento, de cultura, medo de conflito)
49. Já houve situação em que a falta de registro de feedbacks causou problema (por exemplo, numa promoção, num desligamento ou numa discussão sobre desempenho)?
50. Se um sistema pudesse resolver **uma única coisa** do processo atual, o que deveria ser?
51. Existe algo que um sistema de feedback **não** deveria fazer, ou que você considera fora do escopo (por exemplo, denúncias, decisões salariais)?

## 7. Encerramento

*Tempo sugerido: 3 min*

52. Tem algo importante sobre feedback e avaliação na sua organização que não perguntamos?
53. Você conhece alguma ferramenta de feedback ou avaliação que valha a pena analisarmos? Poderia indicar outra pessoa que seria interessante entrevistarmos?
54. Podemos entrar em contato novamente se surgirem dúvidas durante a análise?

Agradecer, confirmar o aceite do termo de consentimento, encerrar a gravação e informar o prazo previsto para a transcrição.

## 8. Checklist pós-entrevista

- [ ] Salvar a gravação em local privado do grupo (não no repositório).
- [ ] Transcrever na íntegra e revisar os trechos com ruído.
- [ ] Criar o arquivo `EntrevistaNN_<Nome>.md` seguindo o modelo da [Entrevista 01](Entrevista01_Adriana.md): identificação, nota sobre a transcrição, sumário com marcações de tempo e seções por tema.
- [ ] Anexar o termo de consentimento assinado (ou registrar o aceite verbal com o tempo da gravação).
- [ ] Listar as dores e etapas do processo para o BPMN (issue #44).
- [ ] Extrair requisitos candidatos com a seção de origem, para a síntese das entrevistas (issue #41) e a matriz de rastreabilidade (issue #49).
- [ ] Registrar novos termos no glossário (issue #53).

## 9. Matriz de cobertura do escopo

| Item do escopo (issue #34) | Bloco | Perguntas |
|---|---|---|
| Tipos de feedback: chefe-colaborador, pares, 360º | B | 6 a 10 |
| Feedback formal, informal, positivo e construtivo | C | 11 a 17 |
| Uso de questionários na avaliação | D | 18 a 23 |
| Análise, indicadores e visualizações desejadas | E | 24 a 28 |
| Confidencialidade e anonimato | F | 29 a 35 |
| Acompanhamento, plano de ação e histórico | G | 36 a 40 |
| Metas e plano de desenvolvimento | H | 41 a 45 |
| Principais dores do processo atual (alimenta o BPMN) | A, I | 1 a 5, 46 a 51 |
| Termo de consentimento do entrevistado (LGPD) | Abertura | [Termo_Consentimento_Entrevista.md](Termo_Consentimento_Entrevista.md) |
