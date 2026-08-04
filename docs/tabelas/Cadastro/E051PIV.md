# E051PIV

## Descrição

Cadastros - Tributos - Partilha do ISS por vigência

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodImp | String(003) | Não | Código do imposto |
| CmpRef | Date | Não | Vigência inicial da partilha |
| PerPar | Number(015,4) | Sim | Percentual partilhado com o município do prestador do serviço |

---

## Chave Primária

- CodImp
- CmpRef

---

## Índices

### E051PIV_FKIndex1

**Tipo:** Não unico

Campos:
- CodImp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
