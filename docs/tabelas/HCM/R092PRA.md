# R092PRA

## Descrição

Proposta de quadro de vagas p/ posto - Roteiro de avaliação

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho da proposta |
| CodPlv | Number(004,0) | Não | Código do plano de vagas da proposta |
| SeqPro | Number(009,0) | Não | Sequencia da proposta de alteração do quadro de vagas por posto |
| SeqPra | Number(003,0) | Não | Sequencia de avaliação da proposta |
| CodCom | Number(004,0) | Sim | Código do Compromisso |
| IniOco | Date | Sim | Data de Início da Ocorrência |
| SeqOco | Number(004,0) | Sim | Sequência da Ocorrência |
| NumEmp | Number(004,0) | Sim | Empresa do avaliador da proposta |
| TipCol | Number(001,0) | Sim | Tipo de colaborador do avaliador da proposta |
| NumCad | Number(009,0) | Sim | Cadastro do avaliador da proposta |
| PosTra | String(024) | Sim | Posto de trabalho onde o avaliador atua |
| SitPra | Number(001,0) | Sim | Situação do passo do roteiro de avaliação |

---

## Chave Primária

- EstPos
- CodPlv
- SeqPro
- SeqPra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092PRA_002

**Tabela:** R092PRO

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |
| SeqPro | SeqPro |

