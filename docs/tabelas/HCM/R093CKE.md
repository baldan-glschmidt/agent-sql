# R093CKE

## Descrição

Controle de Chaves

---

## Resumo

- Campos: 28
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumKey | String(010) | Não | Número da Chave |
| DatRet | Date | Não | Data da Retirada das Chaves |
| HorRet | Number(005,0) | Não | Hora de Retirada das Chaves |
| CodPor | Number(003,0) | Sim | Código da Portaria de Controle das Chaves |
| TipPre | Number(001,0) | Sim | Tipo de pessoa usuária do controle de chave na retirada |
| EmpRet | Number(004,0) | Sim | Empresa que Retirou as Chaves |
| TclRet | Number(001,0) | Sim | Tipo de Colaborador que retirou a chave |
| CadRet | Number(009,0) | Sim | Cadastro do Colaborador que Retirou as Chaves |
| TdvRet | Number(001,0) | Sim | Tipo do Documento do Visitante que Retirou as Chaves |
| NdvRet | String(020) | Sim | Número do Documento do Visitante que Retirou as Chaves |
| ErtOcr | Number(004,0) | Sim | Empresa que Retirou as Chaves |
| OcrRet | Number(009,0) | Sim | Cadastro do Colaborador que Retirou as Chaves |
| DatDev | Date | Sim | Data da Devolução das Chaves |
| HorDev | Number(005,0) | Sim | Hora da Devolução das Chaves |
| TipPde | Number(001,0) | Sim | Tipo de pessoa usuária do controle de chave na devolução |
| EmpDev | Number(004,0) | Sim | Empresa que Devolveu as Chaves |
| TclDev | Number(001,0) | Sim | Tipo de Colaborador que Devolveu as Chaves |
| CadDev | Number(009,0) | Sim | Cadastro do Colaborador que Devolveu as Chaves |
| TdvDev | Number(001,0) | Sim | Tipo do Documento do Visitante que Devolveu as Chaves |
| NdvDev | String(020) | Sim | Número do Documento do Visitante que Devolveu as Chaves |
| EdvOcr | Number(004,0) | Sim | Empresa que Devolveu as Chaves |
| OcrDev | Number(009,0) | Sim | Cadastro do Colaborador Outras Unidades que Devolveu as Chaves |
| ObsRet | String(080) | Sim | Observação na Entrega das Chaves |
| ObsDev | String(080) | Sim | Observação na Devolução das Chaves |
| UsuEnt | Number(010,0) | Sim | Código do Usuário que Entregou as Chaves |
| UsuRec | Number(010,0) | Sim | Código do Usuário que Recebeu as Chaves |
| MatRet | String(010) | Sim | Matrícula do Aluno que retirou a chave |
| MatDev | String(010) | Sim | Matrícula do Aluno que devolveu a chave |

---

## Chave Primária

- NumKey
- DatRet
- HorRet

---

## Índices

### R093CKEindice3

**Tipo:** Não unico

Campos:
- DatDev
- HorDev

---

## Relacionamentos

### IR_R093CKE_000

**Tabela:** R093KEY

| Origem | Destino |
|--------|---------|
| NumKey | NumKey |

