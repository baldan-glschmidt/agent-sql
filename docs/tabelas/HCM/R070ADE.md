# R070ADE

## Descrição

Marcações de Acesso Manuais para o Ato Declaratório

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | String(012) | Não | Número do Crachá |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqAcc | Number(002,0) | Não | Sequência do Registro |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| DirAcc | String(001) | Sim | Direção do Acesso |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| TipDoc | Number(001,0) | Sim | Tipo do documento |
| NumDoc | String(020) | Sim | Número do documento |
| CraVei | Number(012,0) | Sim | Crachá do Veículo |
| ObsMar | String(255) | Sim | Observação da marcação |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DatCad | Date | Sim | Data do Cadastro da Marcação Manual |
| HorCad | Number(005,0) | Sim | Hora do Cadastro da Marcação Manual |
| CPFRes | String(020) | Sim | CPF da pessoa que coletou as info. em formulário papel durante a contingência |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
