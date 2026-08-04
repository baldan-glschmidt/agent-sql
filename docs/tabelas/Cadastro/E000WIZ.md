# E000WIZ

## Descrição

Cadastros - Processo Inicialização (GO UP)

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPrc | Number(002,0) | Não | Código do processo |
| DatIni | Date | Sim | Data do início do processamento |
| HorIni | Number(005,0) | Sim | Hora do inicio do processamento |
| DatFim | Date | Sim | Data do fim do processamento |
| HorFim | Number(005,0) | Sim | Hora do fim do processamento |
| UsuGer | Number(009,0) | Não | Usuário responsável pela geração do registro |
| ObsErr | String(9999) | Sim | Mensagens e Advertências durante o processamento |
| ObsPar | String(9999) | Sim | Parâmetros do Processamento |
| CodSit | Number(001,0) | Não | Situação |

---

## Chave Primária

- CodEmp
- CodFil
- CodPrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
