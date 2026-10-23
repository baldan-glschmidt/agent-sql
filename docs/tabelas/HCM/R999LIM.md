# R999LIM

## Descrição

Dados da Limpeza de Base

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSis | Number(002,0) | Não | Código do Sistema ao Qual o Assunto Pertence |
| CodAss | Number(003,0) | Não | Código do Assunto |
| DatLim | Date | Não | Data da Limpeza |
| HorLim | String(008) | Não | Hora da Limpeza |
| DirBkp | String(255) | Sim | Diretório do Backup |
| ArqBkp | String(018) | Sim | Nome do Arquivo de Backup Gerado na Limpeza |
| CodUsu | Number(004,0) | Sim | Código do Usuário |
| ComLim | String(1024) | Sim | Comentários da Limpeza |
| ParLim | String(512) | Sim | Parâmetros da Limpeza |
| StaLim | Number(001,0) | Sim | Status da Limpeza |
| LimBkp | String(001) | Sim | Limpeza com Backup |
| VerBas | String(015) | Sim | Versão da Base |

---

## Chave Primária

- CodSis
- CodAss
- DatLim
- HorLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
