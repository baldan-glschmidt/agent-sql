# R514DLC

## Descrição

Matriz de Gestão - Linhas/Colunas

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPer | Number(004,0) | Não | Perfil do Formulário de Matriz de Gestão |
| TipDLC | Number(001,0) | Não | Define o tipo de informação (linha/coluna) |
| SeqDLC | Number(002,0) | Não | Define o número da linha/coluna na Matriz de Gestão |
| SigDLC | String(020) | Sim | Define a sigla da linha/coluna |
| RotDLC | String(060) | Sim | Define o rótulo da linha/coluna |
| FaiIni | Number(008,4) | Sim | Define a faixa inicial da linha/coluna |
| FaiFin | Number(008,4) | Sim | Define a faixa final da linha/coluna |

---

## Chave Primária

- CodPer
- TipDLC
- SeqDLC

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R514DLC_000

**Tabela:** R514PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

