# E063BAO

## Descrição

Cadastro de Vínculo de Balança X Operação X Câmera X Finalidade.

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCam | Number(004,0) | Não | Código da Câmera |
| CodBal | Number(004,0) | Não | Código da Balança |
| SeqBao | Number(004,0) | Não | Sequência da Operação de Vínculo |
| OpeBal | Number(001,0) | Não | Operação da Balança |
| FinCam | Number(001,0) | Não | Finalidade da Câmera |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodBal
- SeqBao

---

## Índices

### E063BAOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodBal
- CodCam
- OpeBal

---

## Relacionamentos

Nenhum relacionamento cadastrado.
