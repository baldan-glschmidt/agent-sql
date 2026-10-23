# R058SEP

## Descrição

Separação de Marcações

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor na Separação |
| CodFnc | Number(002,0) | Não | Código da Função na Separação |
| UsoSep | Number(002,0) | Sim | Uso da Marcação Segundo a Separação |
| DirSep | String(001) | Sim | Direção da Marcação Segundo a Separação |
| SitSep | Number(003,0) | Sim | Situação para Marcações de Justificativas |
| TerSai | String(001) | Sim | Término da Situação de Saída Justificada |

---

## Chave Primária

- CodDsp
- CodPlt
- CodRlg
- CodFnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058SEP_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

