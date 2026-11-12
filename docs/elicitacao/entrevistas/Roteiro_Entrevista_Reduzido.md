# Roteiro de Entrevista – Versão Reduzida

**Projeto:** Sistema Web de Feedback e Gestão de Competências
**Disciplina:** Domínios de Software — Bacharelado em Engenharia de Software — Universidade Federal de Goiás (UFG)
**Técnica de elicitação:** Entrevista semiestruturada (versão curta)
**Duração prevista:** 20 a 25 minutos
**Versão completa:** [Roteiro_Entrevista.md](Roteiro_Entrevista.md)
**Termo de consentimento:** [Termo_Consentimento_Entrevista.md](Termo_Consentimento_Entrevista.md)

---

## Quando usar

Use esta versão quando o entrevistado tiver pouco tempo disponível ou quando a entrevista for complementar a outra já realizada. Ela mantém pelo menos uma pergunta por item do escopo da issue #34. A numeração entre parênteses indica a pergunta correspondente na versão completa, para facilitar a comparação entre entrevistas.

Se sobrar tempo, aprofundar com as perguntas marcadas com ↳ ou com o bloco correspondente da versão completa.

## Abertura e consentimento

*2 min*

> Somos alunos da disciplina de Domínios de Software da UFG e estamos levantando requisitos para um sistema de feedback e gestão de competências. A conversa dura cerca de 20 minutos. Com a sua autorização, vamos gravar o áudio para transcrever depois. Seus dados ficam restritos à disciplina, em repositório privado, e você pode pular qualquer pergunta ou pedir a exclusão dos dados a qualquer momento. Você autoriza a gravação?

- [ ] Ler ou entregar o [Termo de Consentimento](Termo_Consentimento_Entrevista.md) e registrar o aceite.
- [ ] Iniciar a gravação só após o aceite.

## Identificação

*1 min*

| Campo | Resposta |
|---|---|
| Nome completo | |
| Função / cargo | |
| Telefone | |
| Porte da organização (nº aproximado de colaboradores) | |
| Papel no processo de avaliação (dá feedback, recebe, administra o ciclo) | |
| Data e entrevistadores | |

## Perguntas

### Processo atual e dores

*5 min · Alimenta o BPMN AS-IS (issue #44)*

1. Conte como funciona o feedback e a avaliação de desempenho na sua organização hoje: quem participa, com que frequência e onde fica registrado. (1, 3)
2. Descreva o caminho de um feedback, desde a decisão de dar até o encerramento. Em que etapa as coisas mais travam ou se perdem? (4, 47)
3. Quais são as três maiores dificuldades do processo hoje? (46)
   - ↳ Já houve problema por falta de registro de feedback (promoção, desligamento, discussão sobre desempenho)? (49)

### Tipos de feedback

*4 min*

4. Quais modalidades acontecem: gestor → colaborador, colaborador → gestor, entre pares, 360º, autoavaliação? Quem decide quem avalia quem? (6, 7)
5. Como você diferencia feedback formal de informal? O informal é registrado em algum lugar? (11)
6. Como um feedback construtivo é conduzido aqui? Ele parte de fatos observados e termina em um plano de ação? E o positivo, cita os fatos e o impacto? (12, 13, 14)

### Questionários e indicadores

*4 min*

7. A avaliação usa um formulário? As perguntas variam por cargo ou por pessoa? Que tipo de pergunta funciona melhor (escala, nota, texto livre)? (18, 19, 20)
8. Como você traduz uma competência ampla, como "comunicação", em algo mensurável? Que indicadores acompanha ou gostaria de acompanhar? (24)
9. Que gráficos ou relatórios seriam mais úteis para você: evolução ao longo do tempo, pontos fortes e a melhorar, comparação autoavaliação × avaliação dos outros, andamento das metas? (26)

### Confidencialidade e anonimato

*3 min*

10. Quem vê hoje os feedbacks de uma pessoa, e quem deveria ver? (29, 30)
11. Em quais modalidades o anonimato faz sentido e em quais atrapalha? Você daria um feedback sincero ao seu gestor se ele soubesse que foi você? (31, 32)
    - ↳ Por quanto tempo os feedbacks devem ficar guardados, inclusive depois que a pessoa sai? (34)

### Acompanhamento, metas e desenvolvimento

*4 min*

12. Depois de um feedback construtivo, é criado um plano de ação? Quem elabora e como ele é acompanhado (check-ins, prazos, verificação final)? (36, 37, 38)
13. Existe histórico dos feedbacks de uma pessoa? Alguém consulta na prática? Para quê? (39)
14. As metas de desenvolvimento são definidas no início do ciclo? Por quem, e com que periodicidade? Como se mede se foram atingidas? (41, 43, 44)

### Fechamento

*2 min*

15. Se um sistema pudesse resolver **uma única coisa** do processo atual, o que deveria ser? E existe algo que ele **não** deveria fazer? (50, 51)
16. Tem algo importante que não perguntamos? Pode indicar outra pessoa ou ferramenta que valha a pena conhecermos? (52, 53)

Agradecer, confirmar o aceite do termo, encerrar a gravação e seguir o [checklist pós-entrevista](Roteiro_Entrevista.md#8-checklist-pós-entrevista) da versão completa.

## Cobertura do escopo

| Item do escopo (issue #34) | Perguntas |
|---|---|
| Tipos de feedback: chefe-colaborador, pares, 360º | 4 |
| Feedback formal, informal, positivo e construtivo | 5, 6 |
| Uso de questionários na avaliação | 7 |
| Análise, indicadores e visualizações desejadas | 8, 9 |
| Confidencialidade e anonimato | 10, 11 |
| Acompanhamento, plano de ação e histórico | 12, 13 |
| Metas e plano de desenvolvimento | 14 |
| Principais dores do processo atual (alimenta o BPMN) | 1, 2, 3, 15 |
| Termo de consentimento do entrevistado (LGPD) | Abertura |
