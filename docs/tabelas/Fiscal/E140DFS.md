# E140DFS

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Serviço - Dispositivos Fiscais

---

## Resumo

- Campos: 19
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIsv | Number(003,0) | Não | Sequência do item de serviço da nota fiscal de saída |
| SeqDis | Number(003,0) | Não | Sequência do dispositivo fiscal do item |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
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
- CodSnf
- NumNfv
- SeqIsv
- SeqDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DFS_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

