# R192GDO

## Descrição

Grupos de Doenças (CID-10)

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCap | Number(002,0) | Não | Capítulo |
| CodGdo | Number(002,0) | Não | Grupo |
| DesGdo | String(300) | Sim | Descrição |
| SubIni | String(003) | Sim | Subgrupo Inicial |
| SubFim | String(003) | Sim | Subgrupo Final |

---

## Chave Primária

- CodCap
- CodGdo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R192GDO_000

**Tabela:** R192CAP

| Origem | Destino |
|--------|---------|
| CodCap | CodCap |

