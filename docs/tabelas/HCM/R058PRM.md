# R058PRM

## Descrição

Permissões de Acesso

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| DesPrm | String(040) | Sim | Descrição da Permissão |
| AcaPrm | String(001) | Sim | Tipo de Ação da Permissão (Lib/Bloq) |
| UtiAlf | String(001) | Sim | Área Alfandegada |
| CodAre | Number(002,0) | Sim | Código da Área Alfandegada |

---

## Chave Primária

- CodPrm

---

## Índices

### R058PRMIndice1

**Tipo:** Não unico

Campos:
- CodAre

---

## Relacionamentos

Nenhum relacionamento cadastrado.
