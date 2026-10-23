# R122AVA

## Descrição

Candidatos Externos - Aprovação Avaliação

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Código do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura do Cargo |
| CodGav | Number(003,0) | Não | Código do Grupo de Avaliação |
| DatGra | Date | Não | Data da Avaliação do Grupo |
| CodUsu | Number(010,0) | Sim | Código do usuário responsável pelo registro |
| UsuApr | Number(010,0) | Sim | Código do usuário aprovador |
| DatApr | Date | Sim | Data da aprovação da avaliação |
| HorApr | Number(005,0) | Sim | Hora da aprovação |
| ObsApr | String(1000) | Sim | Observações sobre aprovação |
| IndApr | Number(001,0) | Sim | Indica a situação da avaliação |

---

## Chave Primária

- NumCan
- EstCar
- CodGav
- DatGra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122AVA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

