# R300ENT

## Descrição

Tela Entrada dos Processos Automáticos

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPat | Number(002,0) | Não | Tipo do Processo Automático |
| CodPro | Number(003,0) | Não | Código do Processo |
| NomVar | String(030) | Não | Nome da Variável da Tela de Entrada |
| CodDst | Number(003,0) | Não | Código do Cadastro do Destinatário |
| SeqVal | Number(002,0) | Não | Sequência do valor |
| TipVar | Number(003,0) | Sim | Tipo da Variável da Tela de Entrada |
| ValNum | Number(015,3) | Sim | Valor da Variável do Tipo Numérica da Tela de Entrada |
| ValStr | String(400) | Sim | Valor da Variável do Tipo String da Tela de Entrada |

---

## Chave Primária

- TipPat
- CodPro
- NomVar
- CodDst
- SeqVal

---

## Índices

### R300ENTIndice2

**Tipo:** Não unico

Campos:
- TipPat
- CodPro
- CodDst

---

## Relacionamentos

### IR_R300ENT_001

**Tabela:** R300PRO

| Origem | Destino |
|--------|---------|
| TipPat | TipPat |
| CodPro | CodPro |

