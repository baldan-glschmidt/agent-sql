# E140EGD

## Descrição

Notas fiscais de saída - Erros de Geração de documento eletrônico

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NUMNFV | Number(009,0) | Não | Número da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| MsgGer | String(999) | Sim | Mensagem da geração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E140EGDIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodSnf
- NUMNFV

---

## Relacionamentos

Nenhum relacionamento cadastrado.
