# E000OBS

## Descrição

Tabelas - Gerais - Observações

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatGer | Date | Não | Data da geração do registro |
| SeqObs | Number(008,0) | Não | Sequência da observação |
| EmpTab | Number(004,0) | Sim | Código da empresa da tabela que recebeu a observação |
| FilTab | Number(005,0) | Sim | Código da filial da tabela que recebeu a observação |
| NomTab | String(010) | Sim | Nome da tabela que recebeu a observação |
| TipObs | String(001) | Não | Tipo da Observação |
| TexObs | String(250) | Não | Texto da observação |
| ProGer | String(010) | Sim | Processo que gerou a observação (Form, Unit, Outros) |
| EmpGer | Number(004,0) | Sim | Código da empresa que gerou o registro |
| FilGer | Number(005,0) | Sim | Código da filial que gerou o registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| TexApr | String(250) | Sim | Texto da Liberação |
| SenApr | String(050) | Sim | Senha para liberação da pendência de aprovação |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela liberação |
| DatApr | Date | Sim | Data da liberação do registro |
| HorApr | Number(005,0) | Sim | Hora da liberação do registro |

---

## Chave Primária

- DatGer
- SeqObs

---

## Índices

### E000OBSIndice2

**Tipo:** Não unico

Campos:
- NomTab
- DatGer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
