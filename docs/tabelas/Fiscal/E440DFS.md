# E440DFS

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Serviço - Dispositivos Fiscais

---

## Resumo

- Campos: 20
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqIsc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqDis | Number(003,0) | Não | Sequência do dispositivo fiscal do item |
| CodDfs | Number(006,0) | Não | Código do dispositivo fiscal |
| BasDfs | Number(015,2) | Sim | Valor base do dispositivo fiscal |
| PerDfs | Number(005,2) | Sim | Percentual do dispositivo fiscal |
| VlrAjs | Number(015,2) | Sim | Valor do ajuste do item referente ao dispositivo fiscal |
| TipReg | String(001) | Sim | Tipo do registro do dispositivo fiscal |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| VlrOut | Number(015,2) | Sim | Outros Valores |
| DesAjs | String(250) | Sim | Descrição do Ajuste |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIsc
- SeqDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DFS_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E440DFS_007

**Tabela:** E051DIS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDfs | CodDfs |

