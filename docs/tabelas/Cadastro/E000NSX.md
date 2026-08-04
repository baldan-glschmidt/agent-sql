# E000NSX

## Descrição

Gerais - Integração de notas fiscais de saída com seniorX

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqItx | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| IdeUni | String(050) | Sim | Identificador único da nota fiscal de saída na integração com seniorX |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| RnvItx | String(001) | Sim | Indicativo se deve reenviar a nota fiscal de saída para integração com seniorX |

---

## Chave Primária

- SeqItx

---

## Índices

### E000NSXIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
