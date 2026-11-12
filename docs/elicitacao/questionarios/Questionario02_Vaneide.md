# Resultado do Questionário 02 – Feedback e Avaliação de Competências

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Técnica de elicitação:** Questionário (Google Forms)
**Data/hora da resposta:** 09/11/2026, 13:25:36 (GMT-3)

---

## 1. Identificação do respondente

| Campo | Resposta |
|---|---|
| Nome completo | Vaneide Neves |
| Telefone | (62) 99804-1588 |
| Cargo / função | Assessoria ao Presidente(CEO) |
| Papel nos processos de avaliação | Gestor ou líder de equipe |
| Porte da empresa | 100 a 499 funcionários |
| Consentimento (LGPD) | Sim, concordo com a participação e com o uso dos dados para esta finalidade |

---

## 2. Perguntas para gestores / RH

| Pergunta | Resposta |
|---|---|
| O que você mais precisa acompanhar sobre a sua equipe? | Planos de ação em andamento |
| Quanto tempo leva para consolidar os resultados de um ciclo de avaliação? | Cerca de 1 semana |

---

## 3. Situação atual do feedback

**Tipos de avaliação dos quais já participou:**
- Avaliação 360° (várias fontes ao mesmo tempo)

**Frequência com que recebe cada tipo de feedback:**

| Tipo de feedback | Frequência |
|---|---|
| Formal (reunião ou ciclo de avaliação) | Às vezes |
| Informal (no dia a dia) | Às vezes |
| Positivo (reconhecimento) | Frequentemente |
| Construtivo (pontos a melhorar) | Às vezes |

**Satisfação com a forma como o feedback acontece hoje:** 3 de 5

**Maiores problemas do processo atual:**
1. Medo de retaliação ao ser sincero
2. Gestores não sabem dar feedback
3. Falta de tempo para avaliar

---

## 4. Confidencialidade e visibilidade

| Pergunta | Resposta |
|---|---|
| Daria um feedback totalmente sincero ao gestor se ele soubesse quem escreveu? (1 a 5) | 1 |
| O que deveria ser anônimo? | Avaliação do gestor feita pelo colaborador |
| Quem deveria ver o resultado da avaliação de uma pessoa? | A própria pessoa avaliada; Gestor direto; RH; Diretoria |

---

## 5. Utilidade dos recursos propostos

| Recurso | Avaliação |
|---|---|
| Dicas de como escrever um feedback construtivo | Muito útil |
| Perguntas adaptadas ao cargo e às competências de cada pessoa | Muito útil |
| Criar um plano de ação com metas a partir do feedback recebido | Muito útil |
| Responder avaliações pelo celular | Muito útil |
| Histórico de todos os feedbacks recebidos | Muito útil |
| Pedir feedback a um colega a qualquer momento, fora do ciclo formal | Útil |
| Lembretes de avaliações pendentes e prazos | Útil |

---

## 6. Painel de resultados e metas

**O que mais gostaria de ver no painel de resultados:**
- Minha autoavaliação comparada à visão dos outros
- Meus pontos fortes e pontos a melhorar
- Comentários recebidos

**Quem deveria definir as metas de desenvolvimento:** Colaborador e gestor juntos

**Tempo aceitável para avaliar um colega:** Mais de 20 minutos

**Se o sistema pudesse resolver UMA coisa:**
> "Sigilo e descrição, normalmente você fica marcado se expor alguns situação."

*(resposta transcrita literalmente)*

---

## 7. Principais pontos observados

- **Sigilo é a preocupação central:** a respondente deu nota 1/5 para a chance de ser sincera com o gestor identificado, apontou "medo de retaliação" como problema e pediu sigilo na pergunta aberta ("você fica marcado se expor alguma situação").
- **Anonimato na avaliação ascendente:** a avaliação do gestor feita pelo colaborador deve ser anônima.
- **Visão de gestora:** precisa acompanhar os planos de ação da equipe, e a consolidação de um ciclo hoje leva cerca de 1 semana, o que indica espaço para automatizar.
- **Experiência com avaliação 360°**, o que sugere que o sistema deve suportar várias fontes de avaliação no mesmo ciclo.
- **Satisfação moderada (3/5):** o reconhecimento é frequente, mas faltam tempo para avaliar e preparo dos gestores.
- **Recursos muito valorizados:** dicas de feedback construtivo, perguntas por cargo/competência, plano de ação, uso pelo celular e histórico.
- **Painel com comparação:** quer ver a própria autoavaliação comparada à visão dos outros, além dos comentários recebidos.
- **Disposta a investir mais tempo** (mais de 20 minutos) para avaliar um colega.

---

## 8. Requisitos derivados deste questionário

Os IDs continuam a numeração do Questionário 01. A coluna "Relação com Q01" indica quando o requisito reforça um já levantado.

| ID | Requisito | Tipo | Origem (seção) | Relação com Q01 |
|---|---|---|---|---|
| RQ-04 | A avaliação do gestor feita pelo colaborador deve ser anônima. | Funcional | 4 | Reforça RQ-04 |
| RQ-13 | A identidade do autor de uma avaliação anônima não deve ser exibida a nenhum perfil, nem ao gestor avaliado. | Não funcional (Segurança / Privacidade) | 3, 4, 6 | Novo |
| RQ-14 | Resultados de avaliações anônimas só devem ser exibidos de forma agregada quando houver um número mínimo de respondentes, para impedir a identificação por exclusão. | Regra de negócio | 4, 6 | Novo (proposta da equipe) |
| RQ-15 | O sistema deve suportar avaliação 360°, reunindo autoavaliação, gestor, pares e liderados no mesmo ciclo. | Funcional | 3 | Novo |
| RQ-16 | O sistema deve consolidar automaticamente os resultados de um ciclo de avaliação ao seu encerramento. | Funcional | 2 | Novo |
| RQ-17 | O gestor deve poder acompanhar o andamento dos planos de ação da sua equipe. | Funcional | 2 | Novo |
| RQ-18 | O painel do colaborador deve comparar sua autoavaliação com a visão dos demais avaliadores. | Funcional | 6 | Novo |
| RQ-19 | O painel do colaborador deve exibir os comentários recebidos. | Funcional | 6 | Complementa RQ-09 e RQ-10 |
| RQ-20 | O sistema deve permitir responder avaliações pelo celular (interface responsiva). | Não funcional (Usabilidade / Portabilidade) | 5 | Novo |
| RQ-21 | O sistema deve enviar lembretes de avaliações pendentes e prazos. | Funcional | 3, 5 | Novo |
| RQ-02 | Perguntas adaptadas ao cargo e às competências de cada pessoa. | Funcional | 5 | Reforça RQ-02 |
| RQ-03 | Dicas para escrever feedback construtivo. | Funcional | 3, 5 | Reforça RQ-03 |
| RQ-06 | Pedir feedback a um colega fora do ciclo formal. | Funcional | 5 | Reforça RQ-06 |
| RQ-07 | Plano de ação com metas a partir do feedback. | Funcional | 5 | Reforça RQ-07 |
| RQ-08 | Metas definidas em conjunto por colaborador e gestor. | Regra de negócio | 6 | Reforça RQ-08 |
| RQ-09 | Histórico de todos os feedbacks recebidos. | Funcional | 5 | Reforça RQ-09 |
| RQ-12 | Registro do consentimento antes da coleta de dados. | Não funcional (LGPD) | 1 | Reforça RQ-12 |

---

## 9. Divergências em relação ao Questionário 01

| Tema | Questionário 01 (Isabella) | Questionário 02 (Vaneide) | Encaminhamento sugerido |
|---|---|---|---|
| Anonimato | "Nada precisa ser anônimo" (mas sinceridade 2/5) | Avaliação do gestor deve ser anônima (sinceridade 1/5) | Manter RQ-04 como obrigatório para a avaliação ascendente |
| Quem vê o resultado | Pessoa avaliada, gestor direto e RH | Inclui também a Diretoria | Validar com a cliente; opção: Diretoria vê apenas dados agregados |
| Responder pelo celular | Nada útil | Muito útil | Manter RQ-20 como requisito de prioridade média |
| Lembretes | Pouco útil | Útil | Manter RQ-21, com opção de desativar |
| Tempo para avaliar | 10 a 20 minutos | Mais de 20 minutos | Manter RQ-11 (até 20 min), que atende às duas |
