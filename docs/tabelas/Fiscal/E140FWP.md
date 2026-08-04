# E140FWP

## Descrição

Integração WMS - Nota Fiscal de Saída - Fila de registros de cancelamento a processar

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| Ideuni | Number(009,0) | Não | Identificador da Fila |
| IdeFwp | Number(009,0) | Não | Identificador de registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- Ideuni

---

## Índices

### E140FWPIndice1

**Tipo:** Não unico

Campos:
- IdeFwp

---

## Relacionamentos

### IR_E140FWP_001

**Tabela:** E140SIW

| Origem | Destino |
|--------|---------|
| IdeFwp | Ideuni |

