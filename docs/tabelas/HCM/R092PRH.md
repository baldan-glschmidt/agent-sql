# R092PRH

## Descrição

Proposta de quadro de vagas p/ posto - Histórico

---

## Resumo

- Campos: 8
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
| SeqHpr | Number(003,0) | Não | Sequencia de avaliação da proposta |
| DthHpr | Number(014,6) | Sim | Data/Hora da alteração da proposta de alteração do quadro |
| CodUsu | Number(009,0) | Sim | Código do usuário responsável pela alteração da proposta |
| ObsHpr | String(2000) | Sim | Observações sobre as alterações realizadas na proposta de alteração do quadro |
| DesHis | String(200) | Sim | Histórico de alterações da proposta |

---

## Chave Primária

- EstPos
- CodPlv
- SeqPro
- SeqHpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092PRH_002

**Tabela:** R092PRO

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |
| SeqPro | SeqPro |

