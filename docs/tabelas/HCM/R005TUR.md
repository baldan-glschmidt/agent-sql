# R005TUR

## Descrição

Turnos do Serviço

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSrv | Number(004,0) | Não | Código do Serviço |
| CodTSe | Number(002,0) | Não | Turno de Serviço |

---

## Chave Primária

- CodSrv
- CodTSe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005TUR_000

**Tabela:** R005SRV

| Origem | Destino |
|--------|---------|
| CodSrv | CodSrv |

### IR_R005TUR_001

**Tabela:** R005TSE

| Origem | Destino |
|--------|---------|
| CodTSe | CodTSe |

