# E440RMD

## Descrição

Compras - Notas Fiscais de Entrada - Rotas do Manifesto Documento Fiscal

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSma | String(003) | Não | Código da série do manifesto |
| NumMan | Number(009,0) | Não | Número do manifesto |
| SeqRmd | Number(003,0) | Não | Sequência da rota no manifesto |
| SeqImd | Number(003,0) | Não | Sequência do item no manifesto |
| TipMov | String(001) | Não | Tipo do movimento de carga e descarga |
| UfsPas | String(002) | Sim | Estado de passagem |
| CepCid | Number(008,0) | Sim | Cep da cidade do movimento |
| SeqEve | Number(004,0) | Sim | Sequência do evento |
| TipEve | Number(006,0) | Sim | Tipo do evento |
| LatCrd | String(050) | Sim | Latitude Carga/Descarga |
| LonCrd | String(050) | Sim | Longitude Carga/Descarga |

---

## Chave Primária

- CodEmp
- CodFil
- CodSma
- NumMan
- SeqRmd
- SeqImd

---

## Índices

### E440RMDIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodSma
- NumMan
- SeqEve
- TipEve

---

## Relacionamentos

Nenhum relacionamento cadastrado.
