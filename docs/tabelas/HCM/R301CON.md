# R301CON

## Descrição

Tabela auxiliar para listar registros da seção K200 do MANAD

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidGer | String(021) | Não | ID da geração |
| SeqReg | Number(015,0) | Não | Sequência do registro |
| DatAlt | Date | Sim | Data da Alteração |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| CfjIns | String(014) | Sim | Número da Inscrição |
| CodEve | Number(004,0) | Sim | Código do Evento |
| CodLoc | String(150) | Sim | Código Centro Custo Contábil ou Local |
| CodCta | String(030) | Sim | Código da Conta Contábil Reduzida |
| CcuTxt | String(100) | Sim | Código Texto C.Custo p/ Exportação |
| DatReg | Date | Sim | Data da geração |

---

## Chave Primária

- PidGer
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
