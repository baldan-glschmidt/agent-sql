# E051IBU

## Descrição

Cadastro de alíquotas do IBS da UF

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador do IBS da UF |
| SigUfs | String(002) | Sim | Estado |
| PerImp | Number(008,4) | Não | Alíquota do IBS da UF |
| VigIni | Date | Não | Vigência inicial |
| DesImp | String(255) | Sim | Descrição do imposto |

---

## Chave Primária

- IdeUni

---

## Índices

### E051IBU_UK

**Tipo:** Unico

Campos:
- SigUfs
- VigIni

### E051IBUIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

Nenhum relacionamento cadastrado.
