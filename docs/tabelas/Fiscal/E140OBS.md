# E140OBS

## Descrição

Vendas - Notas Fiscais de Saída - Observações

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TipInf | Number(001,0) | Não | Tipo de Informação |
| SeqObs | Number(003,0) | Não | Sequência das observações da nota fiscal de saída |
| TipObs | String(001) | Não | Tipo da observação |
| CodMot | Number(006,0) | Sim | Código do motivo da observação |
| ObsNfv | String(1999) | Não | Texto da observação da nota fiscal de saída |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela entrada da observação |
| DatGer | Date | Sim | Data da observação |
| HorGer | Number(005,0) | Sim | Hora da observação |
| CodIdt | String(030) | Sim | Identificação da observação |
| IndObs | Number(001,0) | Sim | Indicativo de qual tipo é a observação (Geral, Fisco ou Contribuinte) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- TipInf
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140OBS_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

