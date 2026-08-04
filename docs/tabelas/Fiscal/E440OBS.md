# E440OBS

## Descrição

Compras - Notas Fiscais de Entrada - Observações

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqObs | Number(003,0) | Não | Sequência das observações da nota fiscal de entrada |
| TipObs | String(001) | Não | Tipo da observação |
| CodMot | Number(006,0) | Sim | Código do motivo da observação |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| CodDft | String(004) | Sim | Código do defeito do produto(não conformidade) |
| CodAco | String(004) | Sim | Código da ação corretiva |
| ObsNfc | String(250) | Não | Observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela entrada da observação |
| DatGer | Date | Sim | Data da observação |
| HorGer | Number(005,0) | Sim | Hora da observação |
| TipDft | String(001) | Sim | Tipo de defeito |
| QtdDft | Number(014,5) | Sim | Quantidade que apresentou o defeito |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440OBS_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

