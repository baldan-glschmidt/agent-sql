# E140HSW

## Descrição

Integração WMS - Nota Fiscal de Saída - Histórico das situações de integração com WMS

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| Ideuni | Number(009,0) | Não | Identificador de registro |
| IdeNws | Number(009,0) | Não | Identificador da situação da integração |
| ObsHis | String(500) | Sim | Observação do histórico da situação |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- Ideuni

---

## Índices

### E140HSWIndice1

**Tipo:** Não unico

Campos:
- IdeNws

---

## Relacionamentos

### IR_E140HSW_001

**Tabela:** E140SIW

| Origem | Destino |
|--------|---------|
| IdeNws | Ideuni |

