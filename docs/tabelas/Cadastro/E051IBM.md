# E051IBM

## Descrição

Cadastro de alíquotas do IBS do Município

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeIbu | Number(009,0) | Não | Identificador do IBS da UF |
| CodRai | Number(007,0) | Sim | Código do município |
| PerImp | Number(008,4) | Não | Alíquota do IBS do município |
| VigIni | Date | Não | Vigência inicial |
| DesImp | String(255) | Sim | Descrição do imposto |

---

## Chave Primária

- IdeUni

---

## Índices

### E051IBM_UK

**Tipo:** Unico

Campos:
- IdeIbu
- CodRai
- VigIni

### E051IBMIndice1

**Tipo:** Não unico

Campos:
- CodRai

### E051IBMIndice2

**Tipo:** Não unico

Campos:
- IdeIbu

---

## Relacionamentos

### IR_E051IBM_001

**Tabela:** E051IBU

| Origem | Destino |
|--------|---------|
| IdeIbu | IdeUni |

