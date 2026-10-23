# R010MOV

## Descrição

Situações - Movimento Sefip

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSit | Number(003,0) | Não | Código da Situação |
| CmpMov | Date | Não | Competência do Movimento |
| CodIni | String(002) | Sim | Código Início Movimento |
| CodRet | String(002) | Sim | Código Retorno Movimento |
| Ini60d | String(002) | Sim | Código Início Movimento < 60d |
| Ret60d | String(002) | Sim | Código Retorno Movimento < 60d |
| IniPro | String(002) | Sim | Cód. Início Movimento Prorrogação |

---

## Chave Primária

- CodSit
- CmpMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010MOV_000

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

