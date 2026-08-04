# E140NEM

## Descrição

Vendas - Notas Fiscais de Saída - Observações de Notas Fiscais Emitidas Manualmente

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
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
| SeqObs | Number(003,0) | Não | Sequência da observação da nota fiscal de saída emitida manualmente |
| ObsNfv | String(250) | Não | Texto da observação da nota fiscal de saída emitida manualmente |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela entrada da observação |
| DatGer | Date | Sim | Data da observação |
| HorGer | Number(005,0) | Sim | Hora da observação |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqObs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140NEM_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

