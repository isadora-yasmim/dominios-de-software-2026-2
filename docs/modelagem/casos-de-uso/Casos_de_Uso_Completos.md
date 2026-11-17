# Casos de Uso Completos

**Projeto:** Sistema de Gestão de Competências (módulo de Feedback)
**Disciplina:** Domínios de Software (2026/2) · 1ª Etapa: Levantamento de Requisitos
**Referência:** Larman, *Utilizando UML e Padrões*, cap. 6
**Issue:** #48 · **Data:** 17/11/2026
**Entrada:** [Diagrama de Casos de Uso](Diagrama_Casos_de_Uso.md) (#47) e [Lista Geral de Requisitos](../../Lista_Geral_Requisitos.md) (#45), versão 1.0

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Distribuição entre os integrantes](#2-distribuição-entre-os-integrantes)
3. [Modelo do caso de uso completo](#3-modelo-do-caso-de-uso-completo)
4. [Convenções de escrita](#4-convenções-de-escrita)
5. [Demais casos de uso em formato resumido](#5-demais-casos-de-uso-em-formato-resumido)

---

## 1. Objetivo

O enunciado pede que o grupo descreva os casos de uso essenciais, com pelo menos um caso de uso completo por integrante (Larman, cap. 6). Esta página reúne as descrições completas e define o modelo que todos seguem. Cada caso de uso fica em um arquivo próprio, nesta mesma pasta.

O formato completo (*fully dressed*) é o mais detalhado dos três formatos de Larman (resumido, informal e completo). Ele mostra todos os passos, as variações e os requisitos que valem para o caso de uso. É usado nos casos de uso mais importantes ou de maior risco, como os sugeridos na seção 9 do diagrama de casos de uso.

---

## 2. Distribuição entre os integrantes

| Caso de uso | Integrante | Por que este caso | Arquivo | Situação |
|---|---|---|---|---|
| UC-25 Exercer direitos de titular | Verônica Ribeiro Oliveira Palmeira | Cobre a LGPD, que é restrição do enunciado. Verônica cuida da LGPD e dos RNF no processo (seção 4.1) | [UC-25_Exercer_Direitos_de_Titular.md](UC-25_Exercer_Direitos_de_Titular.md) | Descrito |
| UC-14 Responder avaliação | Isadora Yasmim da Silva | Mostra o fluxo do avaliador e as regras de confidencialidade e anonimato, que Isadora modelou no modelo ER (#52, seção 10) | [UC-14_Responder_Avaliacao.md](UC-14_Responder_Avaliacao.md) | Descrito |
| _A definir_ | Ana Luísa Pereira dos Santos | | | Pendente |
| UC-08 Registrar feedback | Davi Augusto Ferreira de Carvalho | Núcleo do domínio: emissor, receptor, fatos, tipo e regras de visibilidade. Davi fez o diagrama de casos de uso (#47) e coordena os modelos (seção 4.1) | [UC-08_Registrar_Feedback.md](UC-08_Registrar_Feedback.md) | Descrito |
| _A definir_ | Júlia de Souza Nascimento | | | Pendente |

Ainda sem responsável, entre os sugeridos na seção 9 do diagrama: **UC-13** Planejar ciclo de avaliação e **UC-19** Criar plano de ação. Ao escolher, atualize esta tabela.

---

## 3. Modelo do caso de uso completo

Cada arquivo segue as seções abaixo, na mesma ordem. Os campos são os do modelo completo de Larman. A issue pede o mínimo (nome, ator principal, interessados, pré-condições, garantia de sucesso, cenário principal, extensões, requisitos especiais e frequência). Os outros campos, como escopo, nível e variações de tecnologia, também são de Larman e foram mantidos.

| # | Seção | O que escrever |
|---|---|---|
| — | **Cabeçalho** | ID e nome do diagrama, responsável, data e versão |
| 1 | **Escopo** | O sistema em projeto: "Sistema de Feedback e Gestão de Competências" |
| 2 | **Nível** | "Objetivo do usuário", como todos os casos do diagrama. "Subfunção" só para casos incluídos, como o UC-16 |
| 3 | **Ator principal** | O ator do diagrama que pede o serviço ao sistema para atingir seu objetivo |
| 4 | **Interessados e interesses** | Todos que têm algo a ganhar ou a perder com o caso de uso, mesmo sem usar o sistema, e o que cada um precisa. É daqui que saem as regras que o cenário tem de respeitar |
| 5 | **Pré-condições** | O que precisa ser verdade antes de começar e que o caso de uso **não** verifica |
| 6 | **Garantia de sucesso (pós-condições)** | O que fica verdadeiro ao final, com sucesso, e que atende aos interessados |
| 7 | **Cenário de sucesso principal** | O caminho típico, sem condições nem desvios, em passos numerados |
| 8 | **Extensões** | Todos os outros caminhos, de sucesso ou de falha, ligados ao passo em que acontecem |
| 9 | **Requisitos especiais** | Requisitos não funcionais, atributos de qualidade e restrições que valem para este caso de uso |
| 10 | **Lista de variações de tecnologia e dados** | Formas diferentes de entrada e saída de dados, como formatos de arquivo e canais |
| 11 | **Frequência de ocorrência** | Com que frequência o caso de uso acontece, com a fonte do valor |
| 12 | **Decisões de especificação** | Pontos que as fontes não definiam e que foram decididos ao descrever o caso, com a justificativa. Ocupa o lugar dos "problemas em aberto" de Larman, como na lista geral |
| 13 | **Rastreabilidade** | Requisitos atendidos, entidades do modelo ER, outros casos de uso relacionados e fontes |

---

## 4. Convenções de escrita

**Estilo essencial.** O caso de uso descreve **intenções e responsabilidades**, não a interface. Escreva "O Colaborador escolhe a avaliação", e não "clica no botão Responder". As telas ficam para os protótipos (#50).

**Passos.**

- Cada passo é uma frase com sujeito: "O Avaliador...", "O Sistema...". Alterne ator e sistema.
- Um passo mostra uma interação que faz o processo avançar. Não descreva o que acontece dentro do sistema, a não ser o que importa para os interessados, como gravar ou notificar.
- Cite o requisito entre parênteses quando o passo o atende, por exemplo (RF-019).

**Extensões.** Seguem a numeração de Larman:

- `3a.` é uma condição que pode ocorrer no passo 3. Uma segunda condição no mesmo passo é `3b.`
- A condição é escrita como algo que o sistema ou o ator consegue perceber: "O prazo do convite terminou".
- Os passos dentro da extensão são `3a1.`, `3a2.` e assim por diante.
- A extensão termina dizendo para onde o fluxo vai: "O cenário continua no passo 5" ou "O caso de uso termina".
- `*a.` é uma condição que pode ocorrer **a qualquer momento**.

**Identificadores.**

- Use os IDs e os nomes do [diagrama](Diagrama_Casos_de_Uso.md). Se um nome mudar, atualize também o arquivo `.puml`.
- Decisões de especificação recebem o ID `UCxx-Dnn`, por exemplo `UC25-D01`.
- Requisitos, regras e decisões são citados pelos IDs da lista geral (RF, RNF, RN, P-xx), da especificação suplementar (DS-xx) e do modelo ER (M-xx). Fontes usam as abreviações da lista geral, como E01 §11.

**Nada sem fonte.** Toda regra do caso de uso vem de um requisito, de uma regra de negócio, de um modelo já aprovado ou de uma lei citada na pesquisa documental. Se for preciso decidir algo que as fontes não definem, registre na seção 12 com a justificativa.

**Arquivo.** `UC-xx_Nome_Do_Caso.md`, nesta pasta. Copie um dos casos já descritos como ponto de partida.

---

## 5. Demais casos de uso em formato resumido

Os 31 casos de uso estão descritos em formato resumido, com o cenário principal em uma frase, na [seção 4 do diagrama de casos de uso](Diagrama_Casos_de_Uso.md#4-casos-de-uso), com ator principal, requisitos e prioridade.
