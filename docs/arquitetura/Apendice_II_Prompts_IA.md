# Apêndice II – Prompts de inteligência artificial

**Projeto:** Sistema Web de Feedback e Gestão de Competências · **Etapa:** 2ª Entrega – Arquitetura e Desenho Detalhado
**Versão:** 1.0 · **Issue:** #107 · **Autora:** Isadora Yasmim da Silva · **Revisora:** Ana Luísa Pereira dos Santos

| Item | Descrição |
|---|---|
| Tipo e natureza | Apêndice documental (registro de uso de IA), não é modelo do sistema |
| Propósito | Guardar o prompt completo de cada uso de IA citado nas [referências](Referencias.md), como pede a seção 8 do enunciado |
| Público-alvo | Docente/PO e integrantes do grupo |
| Uso no documento final | Apêndice II do PDF (issue #109). Cada seção é citada na referência correspondente como "Questão: Apêndice II, Seção II.n" |

---

## Como ler este apêndice

- Cada seção corresponde a uma sessão de trabalho com a ferramenta e a uma referência da [seção 8 das referências](Referencias.md#8-uso-de-inteligência-artificial).
- Os prompts estão **literais**, na ordem de envio, com a grafia original (inclusive erros de digitação). Foram copiados do registro local da sessão do Claude Code, e não reescritos de memória.
- Não foram incluídos os avisos automáticos que a extensão do editor anexa às mensagens (arquivo aberto ou trecho selecionado), porque não foram digitados pela integrante.
- O resultado de cada sessão foi revisado pela autora do artefato e é revisado por outro integrante no pull request da issue.
- Um comentário invisível `<!-- sessao: ... -->` guarda o identificador da sessão. O verificador de referências usa essa marca para saber se uma sessão que alterou documentos já foi registrada aqui.

---

## II.1 Modelo de domínio e entidade-relacionamento (#52)
<!-- sessao: 03f8d5cf-5b55-4aad-84ce-a3c42c3d0df1 -->

| Campo | Valor |
|---|---|
| Referência | REF-90 |
| Ferramenta | ANTHROPIC. Claude Code, modelo Claude Opus 5.5. https://claude.com/claude-code |
| Data de acesso | 17 nov. 2026 |
| Integrante | Isadora Yasmim da Silva |
| Artefato | [Modelo de domínio e ER](../modelagem/modelo-dados/Modelo_Dominio_ER.md), versão 1.0 |
| O que a IA fez | Redigiu o modelo e os diagramas em Mermaid a partir da issue e dos artefatos da 1ª etapa. As decisões M-07, M-08 e M-09 foram tomadas pela equipe e informadas nas mensagens 2 e 3 |

**Mensagem 1**

```text
faça a issue 52, use o mermeid pra gerar o diagrama
```

**Mensagem 2** (resposta a perguntas da ferramenta)

```text
Se coletamos a data de nascimento ou só marcamos "menor de idade": coletamos a data de nascimento
Se o resultado consolidado do ciclo é guardado ao encerrar ou calculado a cada consulta: guardado
```

**Mensagem 3**

```text
vamos manter no perfil junto, mas sinalizado que foi em grupo
```

**Mensagem 4**

```text
ótimo, mas você colocou co autoria em tudo, pode tirar, você não pode aparecer como colaborador no github
```

---

## II.2 Planejamento da 2ª etapa e tabela de autoria e revisão (#78)
<!-- sessao: 16e7c2e6-c3ca-4fdb-977f-79c1e1a79ad8 -->

| Campo | Valor |
|---|---|
| Referência | REF-91 |
| Ferramenta | ANTHROPIC. Claude Code, modelo Claude Opus 5.5. https://claude.com/claude-code |
| Data de acesso | 19 nov. 2026 |
| Integrante | Isadora Yasmim da Silva |
| Artefato | Planejamento da 2ª etapa e tabela de autoria e revisão (`docs/arquitetura/Autoria_e_Revisao.md`, PR #114) e seção da 2ª etapa no README |
| O que a IA fez | Redigiu o planejamento e a distribuição de autores e revisores a partir da issue; as mensagens seguintes trazem as decisões do grupo e pedidos de gestão do repositório (PR em rascunho, cartões do Kanban) |

**Mensagem 1**

```text
faça a issue 78
```

**Mensagem 2**

```text
sobre as pendencias: 1- ainda vamos fazer, 2- confirmada, pode colocar nas issues os respectivos revisores, 3- já enviei o convite, mas a professora ainda não aceitou(por isso estamos mantendo o repositorio publico), 4- ainda vamos criar o discord
```

**Mensagem 3**

```text
criei o servidor no discord, o convite pra professora vai ficar pendente até ela compartilhar o usuário dela
```

**Mensagem 4**

```text
crie a pr e deixe como draft, além disso colocque o card em doing
```

**Mensagem 5**

```text
pronto
```

**Mensagem 6**

```text
você comitou o claudelocal.md? ele deve permanecer somente local, não deve estr no repositorio remoto
```

**Mensagem 7**

```text
mova os cards das issue 79, 80, 107 e 108 para coluna a fazer
```

---

## II.3 Decisões arquiteturais e stack tecnológica (#80)
<!-- sessao: 83fa3ce0-f32f-4293-936d-81fbb0bce5c8 -->

| Campo | Valor |
|---|---|
| Referência | REF-92 |
| Ferramenta | ANTHROPIC. Claude Code, modelo Claude Opus 5.5. https://claude.com/claude-code |
| Data de acesso | 22 nov. 2026 |
| Integrante | Isadora Yasmim da Silva |
| Artefato | Decisões arquiteturais (`docs/arquitetura/Decisoes_Arquiteturais.md`, PR #115), versão 1.0 |
| O que a IA fez | Redigiu a primeira versão do documento (stack e ADR-01 a ADR-14) a partir da issue e dos artefatos da 1ª etapa. A escolha das tecnologias foi proposta pela ferramenta e está marcada no documento para confirmação do grupo na revisão |

**Mensagem 1**

```text
implemente a issue 80
```

**Mensagem 2** (resposta à pergunta "Quer que eu faça o push e abra o PR com `Closes #80`, indicando a Verônica como revisora?")

```text
sim
```

---

## II.4 Referências consolidadas, Apêndice II e verificador de referências (#107)
<!-- sessao: ffda9879-0202-4deb-9c6a-35677e947342 -->

| Campo | Valor |
|---|---|
| Referência | REF-93 |
| Ferramenta | ANTHROPIC. Claude Code, modelo Claude Opus 5.5. https://claude.com/claude-code |
| Data de acesso | 22 nov. 2026 |
| Integrante | Isadora Yasmim da Silva |
| Artefato | [Referências](Referencias.md), este apêndice e [`scripts/verificar_referencias.py`](../../scripts/verificar_referencias.py) |
| O que a IA fez | Reuniu as referências que já estavam nas seções de referências dos artefatos, sem acrescentar fontes novas; transcreveu os prompts das sessões anteriores a partir dos registros locais; escreveu o script que aponta referências e prompts ainda não registrados |

**Mensagem 1**

```text
implemente a issue 107, não invente nenhuma referencia, como o trabalho ainda está sendo contruido coloque as que já temos e arrume uma forma de toda vez que uma nova referencia for usada o claude code adicionar ela automaticamente nas referencias
```

---

## Histórico de revisões

| Versão | Data | Autor(a) | Alteração |
|---|---|---|---|
| 1.0 | 22/11/2026 | Isadora Yasmim da Silva | Versão inicial com as seções II.1 a II.4 (issue #107) |
